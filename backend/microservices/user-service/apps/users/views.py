import json
import logging
import os
import uuid

import requests
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
from google.cloud import storage
from user_service.firebase_auth import token_required
from users.models import User, UserPreferences
from users.utils import upload_image_to_bucket

logger = logging.getLogger(__name__)

load_dotenv()

cloud_function_url = os.getenv("CLOUD_FUNCTION_URL")
bucket_name = os.getenv("STORAGE_BUCKET_NAME")
base_url = f"https://storage.googleapis.com/{bucket_name}/"


@csrf_exempt
@token_required
def get_user_profile(request, userid):
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed."}, status=405)
    try:
        user = User.objects.get(id=userid)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found."}, status=404)
    try:
        user_preferences = user.userpreferences
    except UserPreferences.DoesNotExist:
        user.userpreferences = UserPreferences.objects.create(user=user)
        user_preferences = user.userpreferences
        user.userpreferences.save()
    response_data = {
        "id": user.id,
        "name": user.username,
        "img_url": user.img_url,
        "preferences": {
            "data_processing": user_preferences.data_processing_consent,
            "data_sharing": user_preferences.data_sharing_consent,
        },
    }
    return JsonResponse(response_data)


@csrf_exempt
@token_required
def delete_user(request, userid):
    if request.method != "DELETE":
        return HttpResponse(status=405)
    try:
        user = User.objects.get(id=userid)
        user.hard_delete()
        return HttpResponse(status=204)
    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return HttpResponse(status=404)


@csrf_exempt
@token_required
def edit_user_preferences(request, user_id):
    if request.method != "PUT":
        return JsonResponse({"error": "Invalid request method"}, status=405)
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    try:
        data = json.loads(request.body)
        if not data:
            return JsonResponse({"error": "No fields provided for update"}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data"}, status=400)

    # Handle username
    new_username = data.get("username")
    if new_username is not None:
        new_username = new_username.strip()
        if len(new_username) < 6 or len(new_username) > 16:
            return JsonResponse(
                {"error": "Username must be between 6 and 16 characters long"},
                status=400,
            )
        if (
            new_username != user.username
            and User.objects.filter(username=new_username).exists()
        ):
            return JsonResponse({"error": "Username already in use"}, status=400)
        user.username = new_username

    # Handle email
    new_email = data.get("email")
    if new_email is not None:
        new_email = new_email.strip()
        if new_email != user.email and User.objects.filter(email=new_email).exists():
            return JsonResponse({"error": "Email already in use"}, status=400)
        user.email = new_email

    # Handle image
    new_img_url = data.get("img_url", user.img_url)
    if new_img_url is not None:
        user.img_url = new_img_url

    # Handle data processing consent
    dpc = data.get("data_processing_consent")
    if dpc is not None:
        if user.userpreferences:
            user.userpreferences.data_processing_consent = dpc
        else:
            user.userpreferences = UserPreferences.objects.create(
                user=user, data_processing_consent=dpc, data_sharing_consent=True
            )
        user.userpreferences.save()

    # Handle data sharing consent
    dsc = data.get("data_sharing_consent")
    if dsc is not None:
        if user.userpreferences:
            user.userpreferences.data_sharing_consent = dsc
        else:
            user.userpreferences = UserPreferences.objects.create(
                user=user, data_sharing_consent=dsc, data_processing_consent=True
            )
        user.userpreferences.save()
    user.save()
    return JsonResponse(data={}, status=204)


@csrf_exempt
@token_required
def edit_user_image(request, user_id):
    if request.method != "POST":
        return JsonResponse({"error": "Only POST method is accepted"}, status=405)

        # Check if the image part is present in the POST request
    if "image" not in request.FILES:
        return JsonResponse({"error": "No image file provided"}, status=400)

    image_file = request.FILES["image"]
    if image_file.name == "":
        return JsonResponse({"error": "No selected file"}, status=400)

    # Send the image to the GCP AI service
    try:
        response = requests.post(url=cloud_function_url, files={"image": image_file})
        # Check response from AI service
        if response.status_code == 400:
            return JsonResponse(
                {"error": "Image contains inappropriate content"}, status=400
            )
        if response.status_code == 200:
            destination_blob_name = f"users/images/{str(uuid.uuid4())}.jpeg"
            success = upload_image_to_bucket(response.content, destination_blob_name)
            if not success:
                return JsonResponse(
                    {"error": "An error occurred while uploading the image"}, status=500
                )
            # save the user image url
            user = User.objects.get(id=user_id)
            user.img_url = f"{base_url}{destination_blob_name}"
            user.save()
            return JsonResponse(
                {"message": "Profile picture changed successfully"}, status=200
            )
        return JsonResponse(
            {"message": "An error occurred while uploading the image"}, status=500
        )
    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
        # return error message with e as the error message
        return JsonResponse({"error": str(e)}, status=500)

import json
import logging
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from user_service.firebase_auth import token_required
from users.models import User, UserPreferences


logger = logging.getLogger(__name__)


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

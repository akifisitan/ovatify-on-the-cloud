import json
import logging
import uuid
from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from users.models import (
    User,
    UserPreferences,
)
from django.contrib.auth.hashers import check_password


logger = logging.getLogger(__name__)


@csrf_exempt
def login(request):
    if request.method != "POST":
        return HttpResponse(status=405)
    try:
        data = json.loads(request.body.decode("utf-8"))
        email: str = data.get("email")
        password: str = data.get("password")
        user = User.objects.get(email=email)
        if not check_password(password, user.password):
            return JsonResponse({"error": "Invalid credentials"}, status=401)
        user.last_login = timezone.now()
        user.save()
        return JsonResponse({"access": user.id, "refresh": ""}, status=200)
    except User.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)


@csrf_exempt
def create_user(request):
    if request.method != "POST":
        return HttpResponse(status=405)
    try:
        data = json.loads(request.body.decode("utf-8"))
        email: str = data.get("email")
        password: str = data.get("password")
        username: str = data.get("username")
        if not email or not password or not username:
            return JsonResponse({"error": "Missing fields"}, status=400)
        if User.objects.filter(email=email).exists():
            return JsonResponse({"error": "Email already in use"}, status=400)
        userid: str = str(uuid.uuid4())
        user = User(
            id=userid, username=username, email=email, last_login=timezone.now()
        )

        user.set_password(password)
        user.save()
        if not UserPreferences.objects.filter(user=user).exists():
            UserPreferences.objects.create(
                user=user, data_processing_consent=True, data_sharing_consent=True
            )
        return HttpResponse(status=201)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

import base64
import logging
from functools import wraps
from django.http import JsonResponse
from users.models import User
from django.contrib.auth.hashers import check_password
logger = logging.getLogger(__name__)


def validate_token(token: str):
    try:
        # validate token here, for now just using the user id as the token
        user = User.objects.get(id=token)
        return user.id
    except User.DoesNotExist:
        return None
    except Exception as e:
        logger.error(f"Error validating token: {e}")
        return None


def token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return JsonResponse({"error": "No token provided"}, status=401)
        else:
            auth_header = request.META.get('HTTP_AUTHORIZATION')
            token = auth_header.split(' ', 1)
            userid = validate_token(token[1])
            if userid is None:
                return JsonResponse({"error": "Invalid credentials"}, status=401)
            return view_func(request, userid, *args, **kwargs)

    return _wrapped_view

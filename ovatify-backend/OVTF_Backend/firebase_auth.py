import logging
from functools import wraps
from django.http import JsonResponse

logger = logging.getLogger(__name__)


def token_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return JsonResponse({"error": "No token provided"}, status=401)
        else:
            auth_header = request.META['HTTP_AUTHORIZATION']
            bearer_token = auth_header.split(" ")[1]
            userid = 100
            # Call the view function with adding bearer token as a parameter
            return view_func(request, userid, *args, **kwargs)

    return _wrapped_view

from django.urls import path
from users import views


urlpatterns = [
    path("create-user/", view=views.create_user, name="create-user"),
    path("login/", view=views.login, name="login"),
]

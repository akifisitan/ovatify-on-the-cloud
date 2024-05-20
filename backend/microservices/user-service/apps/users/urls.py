from django.urls import path
from users import views

urlpatterns = [
    path("get-user-profile/", view=views.get_user_profile, name="get-user-profile"),
    path("delete-user/", view=views.delete_user, name="delete-user"),
    path(
        "edit-user-preferences/",
        view=views.edit_user_preferences,
        name="edit_user_preferences",
    ),
]

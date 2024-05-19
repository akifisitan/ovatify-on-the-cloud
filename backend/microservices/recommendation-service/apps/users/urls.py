from django.urls import path
from users import views

urlpatterns = [
    path(
        "recommend-you-might-like/",
        view=views.recommend_you_might_like,
        name="recommend-you-might-like",
    ),
    path(
        "recommend-since-you-like/",
        view=views.recommend_since_you_like,
        name="recommend-since-you-like",
    ),
    path(
        "recommend-friend-mix/",
        view=views.recommend_friend_mix,
        name="recommend-friend-mix",
    ),
    path(
        "recommend-friend-listen/",
        view=views.recommend_friend_listen,
        name="recommend-friend-listen",
    ),
]

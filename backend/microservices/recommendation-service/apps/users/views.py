import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from recommendation_service.firebase_auth import token_required
from songs.models import Song
from users.models import (
    User,
    UserPreferences,
    UserSongRating,
    Friend,
)
from users.utils import (
    get_recommendations,
    getFavoriteGenres,
    getFavoriteArtists,
)
import random


logger = logging.getLogger(__name__)


@csrf_exempt
@token_required
def recommend_you_might_like(request, userid):
    try:
        if request.method != "GET":
            return JsonResponse({"error": "Invalid method"}, status=400)
        else:
            data = request.GET
            count = int(data.get("count"))
            if count is None or count < 1 or count > 100:
                return JsonResponse({"error": "Wrong parameter"}, status=400)

            user_songs = UserSongRating.objects.filter(user=userid).order_by("-rating")[
                :20
            ]

            # if user_songs.exists() is False:
            #     return JsonResponse({'error': 'No songs found for the user, cannot make recommendation'}, status=404)

            track_list = []

            for songs in user_songs:
                track_list.append(songs.song.id)

            list(set(track_list))

            if len(track_list) > 5:
                track_list = random.sample(track_list, 5)

            params = {"limit": count, "seed_tracks": track_list}
            # spotify_recommendations = sp.recommendations(**params)
            recommendations = get_recommendations(**params)

            if recommendations["items"] is None:
                return JsonResponse(
                    {
                        "error": "No recommendations based on track can be made currently, please try again later"
                    },
                    status=404,
                )
            # tracks_info = recommendation_creator(spotify_recommendations)
            return JsonResponse(
                {
                    "message": "Recommendation based on track is successful",
                    "tracks_info": recommendations["items"],
                },
                status=200,
            )
    except KeyError as e:
        logging.error(f"A KeyError occurred: {str(e)}")
        return JsonResponse({"error": "KeyError occurred"}, status=500)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)


@csrf_exempt
@token_required
def recommend_since_you_like(request, userid):
    if request.method != "GET":
        return JsonResponse({"error": "Invalid method"}, status=400)
    try:
        data = request.GET
        count = int(data.get("count"))
        if count is None or count < 1 or count > 100:
            return JsonResponse({"error": "Wrong parameter"}, status=404)

        user_genre_seeds = getFavoriteGenres(userid, number_of_songs=20)
        user_genre_seeds = [seed for seed, _ in user_genre_seeds]

        if len(user_genre_seeds) < 2:
            return JsonResponse(
                {"error": "No genre found for the user, cannot make recommendation"},
                status=404,
            )
        user_genre_seeds = user_genre_seeds[:2]

        artist_list = getFavoriteArtists(userid, number_of_songs=20)
        artist_list = [name for name, _ in artist_list]

        if len(artist_list) < 2:
            return JsonResponse(
                {"error": "No artist found for the user, cannot make recommendation"},
                status=404,
            )
        artist_list = artist_list[:2]

        results = {}

        for genre in user_genre_seeds:
            params = {"limit": count, "seed_genres": [genre]}
            recommendations = get_recommendations(**params)
            if recommendations["items"] is None:
                return JsonResponse({"error": recommendations["error"]}, status=404)
            results[genre.title()] = recommendations["items"]

        for artist_name in artist_list:
            params = {"limit": count, "seed_artists": [artist_name]}
            recommendations = get_recommendations(**params)
            if recommendations["items"] is None:
                return JsonResponse({"error": recommendations["error"]}, status=404)
            results[artist_name.title()] = recommendations["items"]

        return JsonResponse(
            {
                "message": "Recommendation based on what you listen is successful",
                "tracks_info": results,
            },
            status=200,
        )
    except KeyError as e:
        logging.error(f"A KeyError occurred: {str(e)}")
        return JsonResponse({"error": "KeyError occurred"}, status=500)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)


@csrf_exempt
@token_required
def recommend_friend_mix(request, userid):
    if request.method != "GET":
        return JsonResponse({"error": "Invalid method"}, status=400)
    try:
        data = request.GET
        count = data.get("count")
        count = int(count)

        if count > 100 or count < 1:
            return JsonResponse({"error": "Invalid count"}, status=400)

        try:
            user = User.objects.get(id=userid)
        except User.DoesNotExist:
            return JsonResponse({"error": "User not found"}, status=404)

        friends_list = Friend.objects.filter(user=user)
        available_friends = []
        for friend in friends_list:
            if (
                UserPreferences.objects.get(user=friend.friend).data_processing_consent
                is True
            ):
                available_friends.append(friend)

        if len(available_friends) < 1:
            return JsonResponse(
                {"error": "No friends found for the user, cannot make recommendation"},
                status=404,
            )

        songs_seed = []
        for friend in available_friends:
            friend_songs = UserSongRating.objects.filter(user=friend.friend).order_by(
                "-rating"
            )
            for song in friend_songs:
                songs_seed.append(song.song.id)

        list(set(songs_seed))

        if len(songs_seed) > 5:
            songs_seed = random.sample(songs_seed, 5)

        elif len(songs_seed) < 1:
            return JsonResponse(
                {"error": "No songs found for friends, cannot make recommendation"},
                status=404,
            )

        params = {"limit": count, "seed_tracks": songs_seed}
        recommendations = get_recommendations(**params)

        if recommendations["items"] is None:
            return JsonResponse(
                {
                    "error": "No recommendations based on friends can be made currently, please try again later"
                },
                status=404,
            )
        return JsonResponse(
            {
                "message": "Recommendation based on friends is successful",
                "tracks_info": recommendations["items"],
            },
            status=200,
        )
    except KeyError as e:
        logging.error(f"A KeyError occurred: {str(e)}")
        return JsonResponse({"error": "KeyError occurred"}, status=500)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)


@csrf_exempt
@token_required
def recommend_friend_listen(request, userid):
    if request.method != "GET":
        return JsonResponse({"error": "Invalid method"}, status=400)
    try:
        data = request.GET
        count = int(data.get("count"))

        if count < 1:
            return JsonResponse({"error": "Invalid count"}, status=400)

        friends = Friend.objects.filter(user=userid)
        friends_list = []

        for user in friends:
            if (
                UserPreferences.objects.get(user=user.friend).data_processing_consent
                is True
            ):
                friends_list.append(user)

        if len(friends_list) < 1:
            return JsonResponse(
                {"error": "No friends found for the user, cannot make recommendation"},
                status=404,
            )

        friend_count = len(friends_list)
        limit = 1
        if count > friend_count:
            limit = count // friend_count
        songs_list = []

        for friend in friends_list:
            friend_songs = UserSongRating.objects.filter(user=friend.friend).order_by(
                "-rating"
            )[:limit]
            for rating in friend_songs:
                song = Song.objects.get(id=rating.song.id)

                track_info = {
                    "name": song.name,
                    "main_artist": [artist.name for artist in song.artists.all()],
                    "release_year": song.release_year,
                    "id": song.id,
                    "img_url": song.img_url,
                }
                songs_list.append(track_info)

        if len(songs_list) > count:
            songs_list = random.sample(songs_list, count)
            return JsonResponse(
                {
                    "message": "Recommendation based on friends is successful",
                    "tracks_info": songs_list,
                },
                status=200,
            )
        if len(songs_list) > 1:
            return JsonResponse(
                {
                    "message": "Recommendation based on friends is successful",
                    "tracks_info": songs_list,
                },
                status=200,
            )
        return JsonResponse(
            {"error": "No songs found for friends, cannot make recommendation"},
            status=404,
        )
    except KeyError as e:
        logging.error(f"A KeyError occurred: {str(e)}")
        return JsonResponse({"error": "KeyError occurred"}, status=500)
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return JsonResponse({"error": "An unexpected error occurred"}, status=500)

from django.urls import path
from users import views


urlpatterns = [
    path("get-all/", view=views.get_all_users, name="get-all-users"),
    path("create-user/", view=views.create_user, name="create-user"),
    path("login/", view=views.login, name="login"),
    path("delete-user/", view=views.delete_user, name="delete-user"),
    path("update-user/", view=views.update_user, name="update-user"),
    path(
        "user-preferences/",
        view=views.user_preferences_create,
        name="user-preferences-create",
    ),
    path("user-songs/", view=views.user_songs_view, name="user-songs-view"),
    path("add-song-rating/", view=views.add_song_rating, name="add-song-rating"),
    path("edit-song-rating/", view=views.edit_song_rating, name="edit-song-rating"),
    path(
        "delete-song-rating/", view=views.delete_song_rating, name="delete-song-rating"
    ),
    path(
        "get-songs-by-genre/", view=views.user_songs_with_genre, name="get-songs-genre"
    ),
    path(
        "get-songs-by-tempo/", view=views.user_songs_with_tempo, name="get-songs-tempo"
    ),
    path(
        "get-songs-by-artist/",
        view=views.user_songs_with_artist,
        name="get-songs-artist",
    ),
    path("get-songs-by-mood/", view=views.user_songs_with_mood, name="get-songs-mood"),
    path(
        "get-recently-added-songs/",
        view=views.get_recently_added_songs,
        name="get-recently-added-songs",
    ),
    path(
        "get-favorite-songs/", view=views.get_favorite_songs, name="get-favorite-songs"
    ),
    path(
        "get-favorite-genres/",
        view=views.get_favorite_genres,
        name="get-favorite-genres",
    ),
    path(
        "get-favorite-artists/",
        view=views.get_favorite_artists,
        name="get-favorite-artists",
    ),
    path(
        "get-favorite-moods/", view=views.get_favorite_moods, name="get-favorite-moods"
    ),
    path(
        "get-favorite-tempos/",
        view=views.get_favorite_tempos,
        name="get-favorite-tempo",
    ),
    path("get-all-recent/", view=views.get_all_recent_songs, name="get-all-recent"),
    path(
        "send-friend-request/",
        view=views.send_friend_request,
        name="send-friend-request",
    ),
    path(
        "get-all-incoming-requests/",
        view=views.get_all_incoming_requests,
        name="get-all-incoming-requests",
    ),
    path(
        "accept-friend-request/",
        view=views.accept_friend_request,
        name="accept-friend-request",
    ),
    path(
        "reject-friend-request/",
        view=views.reject_friend_request,
        name="reject-friend-request",
    ),
    path(
        "get-all-outgoing-requests/",
        view=views.get_all_outgoing_requests,
        name="get-all-outgoing-requests",
    ),
    path(
        "get-incoming-request-count/",
        view=views.get_incoming_requests_count,
        name="get-incoming-count",
    ),
    path("remove-friend/", view=views.remove_friend, name="remove-friend"),
    path("add-friend/", view=views.add_friend, name="add_friend"),
    path(
        "cancel-friend-request/",
        view=views.cancel_friend_request,
        name="cancel-friend-request",
    ),
    path("get-all-friends/", view=views.get_all_friends, name="get-all-friends"),
    path(
        "get-all-global-requests/",
        view=views.get_all_global_requests,
        name="get-all-requests",
    ),
    path("delete-request/", view=views.delete_request, name="delete-request"),
    path(
        "edit-user-preferences/",
        view=views.edit_user_preferences,
        name="edit_user_preferences",
    ),
    path(
        "recommend-you-might-like/",
        view=views.recommend_you_might_like,
        name="recommend-you-might-like",
    ),
    path("get-user-profile/", view=views.get_user_profile, name="get-user-profile"),
    path(
        "get-recent-addition-counts/",
        view=views.get_recent_addition_by_count,
        name="get-recent-addition-count",
    ),
    path("get-profile-stats/", view=views.get_profile_stats, name="get-profile-stats"),
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
    path("export-by-genre/", views.export_by_genre, name="export-by-genre"),
    path("export-by-artist/", views.export_by_artist, name="export-by-artist"),
    path(
        "get-library-artist-names/",
        views.get_library_artist_names,
        name="get-library-artist-names",
    ),
    path(
        "get-library-genre-names/",
        views.get_library_genre_names,
        name="get-library-genre-names",
    ),
    path("upload-file/", views.import_song_JSON, name="import-song-json"),
    path(
        "get-all-data-sharing-friends/",
        views.get_all_data_sharing_friends,
        name="get-all-data-sharing-friends",
    ),
    path(
        "get-friends-favorite-genres/",
        views.get_friends_favorite_genres,
        name="get-friends-favorite-genres",
    ),
    path(
        "get-friends-favorite-artists/",
        views.get_friends_favorite_artists,
        name="get-friends-favorite-artists",
    ),
    path(
        "get-friends-favorite-moods/",
        views.get_friends_favorite_moods,
        name="get-friends-favorite-moods",
    ),
    path(
        "get-friends-favorite-tempos/",
        views.get_friends_favorite_tempos,
        name="get-friends-favorite-tempos",
    ),
    path(
        "get-friends-recent-addition-counts/",
        views.get_friends_recent_addition_by_count,
        name="get-friends-recent-addition-count",
    ),
    path("get-playlists/", views.get_playlists, name="get_playlists"),
    path("get-playlist-by-id/", views.get_playlist_by_id, name="get_playlist_by_id"),
    path(
        "add-song-to-playlist/", views.add_song_to_playlist, name="add_song_to_playlist"
    ),
    path(
        "remove-song-from-playlist/",
        views.remove_song_from_playlist,
        name="remove_song_from_playlist",
    ),
    path(
        "create-empty-playlist/",
        views.create_empty_playlist,
        name="create_empty_playlist",
    ),
    path("delete-playlist/", views.delete_playlist, name="delete_playlist"),
    path("edit-playlist/", views.edit_playlist, name="edit_playlist"),
    path(
        "get-global-all-friend-groups/",
        views.get_global_all_friend_groups,
        name="get-global-all-friend-groups",
    ),
    path("create-friend-group/", views.create_friend_group, name="create-friend-group"),
    path(
        "get-friend-group-by-id/",
        views.get_friend_group_by_id,
        name="get-friend-group-by-id",
    ),
    path("add-friend-to-group/", views.add_friend_to_group, name="add-friend-to-group"),
    path(
        "remove-friend-from-group/",
        views.remove_friend_from_group,
        name="remove-friend-from-group",
    ),
    path("delete-friend-group/", views.delete_friend_group, name="delete-friend-group"),
    path("edit-friend-group/", views.edit_friend_group, name="edit-friend-group"),
    path(
        "get-all-friend-groups-of-user/",
        views.get_all_friend_groups_of_user,
        name="get-all-friend-groups-of-user",
    ),
    path(
        "get-playlists-of-group/",
        views.get_playlists_of_group,
        name="get-playlists-of-group",
    ),
    path(
        "create-empty-playlist-in-group/",
        views.create_empty_playlist_in_group,
        name="create-empty-playlist-in-group",
    ),
    path(
        "delete-playlist-from-group/",
        views.delete_playlist_from_group,
        name="delete-playlist-from-group",
    ),
    path("suggest-song/", views.suggest_song, name="suggest-song"),
    path("get-suggestions/", views.get_suggestions, name="get-suggestions"),
    path(
        "get-suggestion-count/", views.get_suggestion_count, name="get-suggestion-count"
    ),
    path("set-suggestion-seen/", views.set_suggestion_seen, name="set-suggestion-seen"),
    path("delete-suggestion/", views.delete_suggestion, name="delete-suggestion"),
    path("save-playlist/", views.save_playlist, name="save_playlist"),
]

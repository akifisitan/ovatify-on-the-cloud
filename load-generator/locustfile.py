from locust import FastHttpUser, between, task


class WebsiteUser(FastHttpUser):
    wait_time = between(3, 5)  # Wait time between tasks

    def on_start(self):
        self.login()

    # Auth Service Tests

    def login(self):
        response = self.client.post(
            "/login", json={"email": "a@a.com", "password": "password"}
        )
        token = response.json()["token"]
        # self.client.headers.update({"Authorization": f"Bearer {token}"})
        # have not tested to see if it works yet
        self.client.auth_header = f"Bearer {token}"

    # Recommendation Service Tests

    @task
    def recommend_you_might_like(self):
        self.client.get("/users/recommend-you-might-like/")

    @task
    def recommend_since_you_like(self):
        self.client.get("/users/recommend-since-you-like/")

    @task
    def recommend_friend_mix(self):
        self.client.get("/users/recommend-friend-mix/")

    @task
    def recommend_friend_listen(self):
        self.client.get("/users/recommend-friend-listen/")

    # User Service Tests

    @task
    def get_user_profile(self):
        self.client.get("/users/get-user-profile/")

    @task
    def edit_user_preferences(self):
        self.client.put("/users/edit-user-preferences/", json={"user": "wow"})

    @task
    def edit_user_image(self):
        self.client.post("/users/edit-user-image/", files={})

    # Mono Service Tests

    @task
    def mono_serv(self):
        self.client.get("/")

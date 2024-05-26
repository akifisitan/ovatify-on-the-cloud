import uuid
from locust import FastHttpUser, between, task


class WebsiteUser(FastHttpUser):
    wait_time = between(3, 5)  # Wait time between tasks

    def on_start(self):
        self.login()

    # Auth Service Tests

    def login(self):
        response = self.client.post(
            "/users/login", json={"email": "a@a.com", "password": "password"}
        )
        token = response.json()["access"]
        # self.client.headers.update({"Authorization": f"Bearer {token}"})
        # have not tested to see if it works yet
        self.client.auth_header = f"Bearer {token}"

    # Recommendation Service Tests

    @task
    def recommend_you_might_like(self):
        self.client.get("/users/recommend-you-might-like/?count=10")

    @task
    def recommend_since_you_like(self):
        self.client.get("/users/recommend-since-you-like/?count=10")

    @task
    def recommend_friend_mix(self):
        self.client.get("/users/recommend-friend-mix/?count=10")

    @task
    def recommend_friend_listen(self):
        self.client.get("/users/recommend-friend-listen/?count=10")

    # User Service Tests

    @task
    def get_user_profile(self):
        self.client.get("/users/get-user-profile/")

    # @task
    # def edit_user_preferences(self):
    #     self.client.put("/users/edit-user-preferences/", json={"user": "wow"})

    @task
    def edit_user_image(self):
        filename="image.png"
        with open(filename, "rb") as image:  # Replace 'test_image.jpg' with your image file's name
            files = {'image': image}
            self.client.post("/users/edit-user-image/", files=files)

    # Mono Service Tests

    @task
    def mono_serv(self):
        self.client.get("/")

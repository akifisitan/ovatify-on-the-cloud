from locust import FastHttpUser, between, task


class WebsiteUser(FastHttpUser):
    wait_time = between(3, 5)

    @task
    def index(self):
        self.client.get("/")

    @task
    def explore(self):
        self.client.get("/explore")

    @task
    def library(self):
        self.client.get("/library")

    @task
    def stats(self):
        self.client.get("/stats")

    @task
    def profile(self):
        self.client.get("/profile")

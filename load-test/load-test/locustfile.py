from locust import FastHttpUser, task

class User(FastHttpUser):
    @task
    def hello_world(self):
        self.client.get("/")
import requests
from locust import HttpUser, FastHttpUser, task, User


class TestUser(FastHttpUser):
    # host = "http://35.185.239.229:30004"

    @task
    def main_page(self):
        self.client.get("/", headers={'Connection': 'close'})
        # url = self.host + "/"
        # requests.get(url)

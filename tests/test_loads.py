from locust import HttpUser, between, task


class WebsiteUser(HttpUser):
    wait_time = between(0.5, 1)

    @task
    def profile(self):
        self.client.get("/server2server/ad.json?storeHash=cd8def3ab0e5bffccf6aaab750dad84b&signal=Hanglampen&widgets=product_page_w1&pageType=search&cookie=mbinterviewest", name="/server2server/ad.json")

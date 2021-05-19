from tests import BaseTest, TestCase, pytest
from helpers.lambdas import stamp
from api.oems.server_2_server import Server2ServerApi


class TestServer2ServerApi(BaseTest, TestCase):

    api = None

    def setUp(self) -> None:
        self.api = Server2ServerApi()

    def test_check_response_time_take_less_then_1_second(self):
        self.api.set_api_query_params()
        start_time = stamp()
        response = self.api.request("GET", self.api.get_url())
        process_time = stamp() - start_time
        data = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(data)
        self.assertLess(process_time, 1)

    def test_load_100_requests(self):
        self.api.set_api_query_params()
        sum = 0
        for i in range(100):
            start_time = stamp()
            self.api.request("GET", self.api.get_url())
            sum += start_time - start_time
        sum_avg = sum / 100
        self.assertLess(sum_avg, 1)


if __name__ == "__main__":
    pytest.main()

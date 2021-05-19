from helpers.manager import DriverManager
from unittest import TestCase
import pytest


class BaseTest(TestCase):

    driver = None

    def setUp(self) -> None:
        self.driver = DriverManager.create_driver(DriverManager.CHROME)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

if __name__ == "__main__":
    pytest.main()

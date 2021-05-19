from tests import BaseTest, TestCase, pytest
from ui.pages.login_page import LoginPage
from ui.pages.dashboard_page import DashboardPage


class TestLogin(BaseTest, TestCase):

    def test_login_success(self):
        try:
            page = LoginPage(self.driver)
            status = page.login()
            self.assertTrue(status)
            page = DashboardPage(self.driver)
            status = page.logout()
            self.assertTrue(status)
        except AssertionError as e:
            self.fail(e.with_traceback(e.__traceback__))
        finally:
            ...

if __name__ == '__main__':
    pytest.main()

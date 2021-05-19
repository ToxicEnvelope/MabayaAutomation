from ui.pages import BasePage
from ui.locators.dashboard_page_locators import DashboardPageLocators


class DashboardPage(BasePage, DashboardPageLocators):

    identifier = None
    loaded = False

    def __init__(self, driver=None):
        super(DashboardPage, self).__init__(driver=driver)
        self.identifier = self.IDENTIFIER
        self.wait_for_page_to_load()

    def logout(self):
        final_locator = self.build_locator(self.CURRENT_LOGGED_USER_QUERY, self.std.login_user.split('@')[0])
        if not self.click(locator=final_locator):
            return False
        if not self.click(self.SIGN_OUT_LINK):
            return False
        return True

    def get_current_logged_user(self):
        current_logged_in_user = self.get_text(self.identifier)
        if not current_logged_in_user:
            return False
        return current_logged_in_user

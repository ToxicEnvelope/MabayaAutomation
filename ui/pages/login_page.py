from ui.pages import BasePage
from ui.locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):

    def __init__(self, driver=None):
        super(LoginPage, self).__init__(driver=driver)
        self.identifier = self.IDENTIFIER

    def login(self, email=None, password=None, remember_me=False):
        self.navigate()
        if not self.wait_for_page_to_load():
            return False
        if not email:
            email = self.std.login_user
        if not password:
            password = self.std.login_password
        if not self.set_text(self.USERNAME_INPUT, email):
            return False
        if not self.set_text(self.PASSWORD_INPUT, password):
            return False
        if remember_me:
            if not self.click(self.REMEMBER_CHECKBOX):
                return False
        if not self.click(self.SIGN_IN_BTN):
            return False
        return True

    def get_error_messages(self):
        invalid_user = self.get_text(self.USERNAME_MISSING_DIV)
        invalid_pass = self.get_text(self.PASSWORD_MISSING_DIV)
        if not(invalid_pass or invalid_user):
            return False
        return invalid_pass, invalid_user

    def forgot_password(self):
        if not self.click(self.FORGOT_PASSWORD_LINK):
            return False
        return True

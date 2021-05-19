from ui.pages import BasePage
from ui.locators.forgot_page_locators import ForgotPageLocators


class ForgotPage(BasePage, ForgotPageLocators):
    
    def __init__(self, driver=None):
        super(ForgotPage, self).__init__(driver=driver)

    def reset_password(self, email=None):
        if not email:
            email = self.std.login_user
        if not self.set_text(self.EMAIL_INPUT, email):
            return False
        if not self.click(self.SUBMIT_MAIL_BTN):
            return False
        return True

    def get_error_messages(self):
        invalid_email = self.get_text(self.EMAIL_MISSING_DIV)
        if not invalid_email:
            return False
        return invalid_email

    def back_to_login(self):
        if not self.click(self.BACK_TO_LOGIN_LINK):
            return False
        return True

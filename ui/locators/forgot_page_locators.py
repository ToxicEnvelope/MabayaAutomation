from selenium.webdriver.common.by import By


class ForgotPageLocators:
    EMAIL_INPUT = (By.ID, "auth-forgot-email")
    SUBMIT_MAIL_BTN = (By.CSS_SELECTOR, "button[type='submit']")
    BACK_TO_LOGIN_LINK = (By.CSS_SELECTOR, "a[routerlink='/auth/login']")
    EMAIL_MISSING_DIV = (By.CSS_SELECTOR, "div[translate='page.auth.v_email']")

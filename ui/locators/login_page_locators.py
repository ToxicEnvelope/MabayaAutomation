from selenium.webdriver.common.by import By


class LoginPageLocators:
    IDENTIFIER = (By.ID, "auth-container")
    USERNAME_INPUT = (By.ID, "auth-login-email")
    USERNAME_MISSING_DIV = (By.CSS_SELECTOR, "div[translate='page.auth.v_email']")
    PASSWORD_INPUT = (By.ID, "auth-login-password")
    PASSWORD_MISSING_DIV = (By.ID, "div[translate='page.auth.v_password']")
    FORGOT_PASSWORD_LINK = (By.CSS_SELECTOR, "a[routerlink='/auth/forgot']")
    REMEMBER_CHECKBOX = (By.ID, "auth-login-remember")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "button[type='submit']")

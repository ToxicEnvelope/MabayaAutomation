from selenium.webdriver.common.by import By


class DashboardPageLocators:
    IDENTIFIER = (By.ID, "backoffice-logo")
    CURRENT_LOGGED_USER_QUERY = (By.XPATH, '//*[contains(text(), "%e%")]')
    SIGN_OUT_LINK = (By.CSS_SELECTOR, "div#header-main-dropdown-menu > a[href='/']")

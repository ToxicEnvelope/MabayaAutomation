from typing import Optional
from selenium.webdriver.remote.webdriver import WebDriver, WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
from helpers import SuiteTestData


class BasePage:

    browser = None
    std = None
    identifier = None
    loaded = None

    def __init__(self, driver: WebDriver):
        self.browser = driver
        self.std = SuiteTestData()

    def wait_for_page_to_load(self, retries=5):
        try:
            if retries == 0:
                return False
            found = self.find_element(locator=self.identifier)
            if found:
                return True
            retries -= 1
            return self.wait_for_page_to_load(retries=retries)
        except Exception as e:
            return False

    def navigate(self, url=None):
        try:
            if not url:
                url = self.std.login_url
            self.browser.get(url)
        except (Exception, WebDriverException) as e:
            return False

    def click(self, locator=None, use_js=False, use_action_chain=False, multiple=False):
        try:
            if not locator:
                return False
            if multiple:
                elements = self.find_element(locator=locator, multiple=multiple)
                if use_js:
                    for element in elements:
                        self.browser.execute_script("arguments[0].click();", element)
                elif use_action_chain:
                    for element in elements:
                        ActionChains(driver=self.browser).click(on_element=element).perform()
                else:
                    for element in elements:
                        element.click()
            else:
                element = self.find_element(locator=locator)
                if use_js:
                    self.browser.execute_script("arguments[0].click();", element)
                elif use_action_chain:
                    ActionChains(driver=self.browser).click(on_element=element).perform()
                else:
                    element.click()
            return True
        except (Exception, WebDriverException, StaleElementReferenceException) as e:
            return False

    def set_text(self, locator=None, text=None, use_js=False, use_action_chain=False, multiple=False):
        try:
            if not locator:
                return False
            if multiple:
                elements = self.find_element(locator=locator, multiple=multiple)
                if len(elements) == 0:
                    return False
                if use_js:
                    for element in elements:
                        self.browser.execute_script(f"arguments[0].value={text};", element)
                elif use_action_chain:
                    for element in elements:
                        ActionChains(driver=self.browser).send_keys_to_element(element, text).perform()
                else:
                    for element in elements:
                        element.send_keys(text)
            else:
                element = self.find_element(locator=locator)
                if not element:
                    return False
                if use_js:
                    self.browser.execute_script(f"arguments[0].value={text};", element)
                elif use_action_chain:
                    ActionChains(driver=self.browser).send_keys_to_element(element, text).perform()
                else:
                    element.send_keys(text)
            return True
        except (Exception, WebDriverException, StaleElementReferenceException) as e:
            return False

    def find_element(self, locator=None, multiple=False) -> Optional[WebElement]:
        try:
            if not locator:
                return False
            if multiple:
                return WebDriverWait(
                    driver=self.browser,
                    timeout=30,
                    poll_frequency=0.250
                ).until(EC.presence_of_all_elements_located(locator=locator))
            else:
                return WebDriverWait(
                    driver=self.browser,
                    timeout=30,
                    poll_frequency=0.250
                ).until(EC.presence_of_element_located(locator=locator))
        except (Exception, WebDriverException) as e:
            return False

    def get_text(self, locator=None, multiple=False, use_js=False):
        try:
            result = None
            if not locator:
                return False
            if multiple:
                txt_results = []
                elements = self.find_element(locator=locator, multiple=multiple)
                if len(elements) == 0:
                    return False
                if use_js:
                    for element in elements:
                        txt = self.browser.execute_script("return arguments[0].value;", element)
                        txt_results.append(txt)
                else:
                    for element in elements:
                        txt_results.append(element.text)
                result = txt_results
            else:
                element = self.find_element(locator=locator)
                if not element:
                    return False
                if use_js:
                    result = self.browser.execute_script("return arguments[0].value;", element)
                else:
                    result = element.text
            return result
        except (Exception, WebDriverException, StaleElementReferenceException) as e:
            return False

    def build_locator(self, locator=None, replace_value=None):
        try:
            if not locator:
                return False
            by, value = locator
            value = value.replace('%e%', replace_value)
            return by, value
        except Exception as e:
            return False

    def get_error_messages(self): pass

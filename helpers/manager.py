from selenium import webdriver
from os.path import join, dirname, abspath


class Resources:
    __resources_folder__ = join(dirname(dirname(abspath(__file__))), 'resources')
    __binary_folder__ = join(dirname(dirname(abspath(__file__))), 'bin')

    @staticmethod
    def get_resource(resource_name):
        try:
            return join(Resources.__resources_folder__, resource_name)
        except Exception as e:
            return False

    @staticmethod
    def get_bin(driver_binary):
        try:
            binary = None
            if driver_binary == 1:
                binary = "chromedriver"
            elif driver_binary == 2:
                binary = "chromedriver"
            elif driver_binary == 3:
                binary = "chromedriver"
            elif driver_binary == 4:
                binary = "chromedriver"
            elif driver_binary == 5:
                binary = "chromedriver"
            else:
                return False
            return join(Resources.__binary_folder__, binary)
        except Exception as e:
            return False


class DriverManager:
    CHROME = 1
    FIREFOX = 2
    OPERA = 3
    EDGE = 4
    PHANTOM_JS = 5

    @staticmethod
    def create_driver(driver_type):
        driver = None
        if driver_type == DriverManager.CHROME:
            driver = webdriver.Chrome(Resources.get_bin(DriverManager.CHROME))
        elif driver_type == DriverManager.FIREFOX:
            driver = webdriver.Chrome(Resources.get_bin(DriverManager.FIREFOX))
        elif driver_type == DriverManager.OPERA:
            driver = webdriver.Chrome(Resources.get_bin(DriverManager.OPERA))
        elif driver_type == DriverManager.EDGE:
            driver = webdriver.Chrome(Resources.get_bin(DriverManager.EDGE))
        elif driver_type == DriverManager.PHANTOM_JS:
            driver = webdriver.Chrome(Resources.get_bin(DriverManager.PHANTOM_JS))
        else:
            return False
        return driver

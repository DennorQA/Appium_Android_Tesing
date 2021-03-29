from Settings.Config import Config
from appium import webdriver


class init_test:

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def setup_driver(self):
        self.driver = webdriver.Remote(Config.HOST, Config.DESIRED_CAP)
        self.driver.implicitly_wait(5)

        return self.driver

    @staticmethod
    def tear_down(self):
        self.driver.quit()

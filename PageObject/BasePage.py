from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def conditions(self, by_locator):
        condition = ec.visibility_of_element_located(by_locator)
        element = WebDriverWait(self.driver, self.timeout).until(condition)

        return element

    def tap(self, by_locator):
        element = self.conditions(by_locator)
        element.click()

    def get_list_of_elements(self, by_locator):
        list_of_elements = []
        elements = self.driver.find_elements_by_class_name(by_locator)
        for element in elements:
            list_of_elements.append(element.text)

        return list_of_elements

    def send_keys(self, by_locator, value):
        element = self.conditions(by_locator)
        element.send_keys(value)

    def get_element_text(self, by_locator):
        element = self.conditions(by_locator)

        return element.text

    def is_displayed(self, by_locator):
        element = self.conditions(by_locator)

        return bool(element)

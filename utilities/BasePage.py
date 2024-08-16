import inspect
import logging

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BasePage:

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)

        return logger

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        element = self.find_element(*locator)
        element.click()

    def set(self, locator, value):
        element = self.find_element(*locator)
        element.clear()
        element.send_keys(value)

    def verify_link_presence(self, text):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def verify_id_presence(self, text):
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.ID, text)))

    def verify_text_presence(self, text):
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def verify_text_not_presence(self, text):
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))

    def verify_locator_invisibility(self, value):
        WebDriverWait(self.driver, 30).until_not(EC.visibility_of_element_located(value))

    def visibility_of_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))

    def assert_element_present(self, locator):
        try:
            self.find_element(*locator)
            assert True, f"Element {locator} is present on the page."
        except NoSuchElementException:
            assert False, f"Element {locator} is not present on the page."

    def assert_element_not_present(self, locator):
        try:
            self.find_element(*locator)
            assert False, f"Element {locator} is present on the page."
        except NoSuchElementException:
            assert True, f"Element {locator} is not present on the page."

    def get_text(self, locator):
        element = self.find_element(*locator)
        return element.text

    def is_visible(self, locator):
        try:
            element = self.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False

    def text_present_in_element(self, locator, text):
        WebDriverWait(self.driver, 10).until(
            EC.text_to_be_present_in_element(locator, text)
        )

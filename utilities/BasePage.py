import inspect
import logging

import pytest
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BasePage:

    def get_logger(self):

        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)

        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        return self.find_element(*locator).click()

    def set(self, locator, value):
        self.find_element(*locator).clear()
        self.find_element(*locator).send_keys(value)

    def verify_link_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def verify_id_presence(self, text):
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, text)))

    def verify_text_presence(self, text):
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def verify_text_not_presence(self, text):
        locator = (By.XPATH, f"//*[contains(text(), '{text}')]")
        element = WebDriverWait(self.driver, 10).until_not(EC.presence_of_element_located(locator))

    def verify_locator_invisibility(self, value):
        element = WebDriverWait(self.driver, 10).until_not(EC.visibility_of_element_located(value))

    def verify_locator_visibility(self, value):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(value))

    def assert_element_present(self, locator):
        try:
            element = self.find_element(*locator)
            assert True, f"Element {locator} is present on the page."
        except NoSuchElementException:
            assert False, f"Element {locator} is not present on the page."

    def assert_element_not_present(self, locator):
        try:
            element = self.find_element(*locator)
            assert False, f"Element {locator} is present on the page."
        except NoSuchElementException:
            assert True, f"Element {locator} is not present on the page."

    def get_text(self, locator):
        return self.find_element(*locator).text

    def is_visible(self, locator):
        try:
            element = self.find_element(*locator)
            return element.is_displayed()
        except NoSuchElementException:
            return False, "Element is not visible"

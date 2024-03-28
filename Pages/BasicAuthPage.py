from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class BasicAuth(BasePage):
    message = (By.CSS_SELECTOR, "div.example p")

    def __init__(self, driver):
        self.driver = driver

    def open_page(self, username, password):
        url = f"https://{username}:{password}@the-internet.herokuapp.com/basic_auth"
        self.driver.get(url)

    def get_message(self):
        message_text = self.get_text(self.message)
        return message_text


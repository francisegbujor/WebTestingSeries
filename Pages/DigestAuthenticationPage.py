from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class DigestAuthentication(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    message = (By.CSS_SELECTOR, "div.example p")

    def __init__(self, driver):
        self.driver = driver

    def open_digest_authentication_page(self, username, password):
        url = f"https://{username}:{password}@the-internet.herokuapp.com/digest_auth"
        self.driver.get(url)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_message(self):
        message_text = self.get_text(self.message)
        return message_text
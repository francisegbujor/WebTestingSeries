from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class ExitIntent(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    modal = (By.CLASS_NAME, "modal")
    modal_title = (By.CSS_SELECTOR, "div[class='modal-title'] h3")
    close_button = (By.XPATH, "(//p[normalize-space()='Close'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def open_exit_intent_page(self):
        home = HomePage(self.driver)
        return self.click(home.exitIntentLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_modal_title(self):
        title_text = self.get_text(self.modal_title)
        return title_text

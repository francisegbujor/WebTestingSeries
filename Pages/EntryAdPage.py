from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class EntryAd(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    click_here_link = (By.LINK_TEXT, "click here")
    window_title = (By.CSS_SELECTOR, "div[class='modal-title'] h3")
    close_button = (By.XPATH, "(//p[normalize-space()='Close'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def open_entry_ad_page(self):
        home = HomePage(self.driver)
        return self.click(home.entryAdLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_window_title(self):
        title_text = self.get_text(self.window_title)
        return title_text

from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class Frames(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    nested_frames_link = (By.LINK_TEXT, "Nested Frames")
    left_frame = (By.TAG_NAME, "body")
    bottom_frame = (By.TAG_NAME, "body")

    def __init__(self, driver):
        self.driver = driver

    def open_frames_page(self):
        home = HomePage(self.driver)
        return self.click(home.framesLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_text_from_left_frame(self):
        return self.find_element(*self.left_frame).text

    def get_text_from_bottom_frame(self):
        return self.find_element(*self.bottom_frame).text
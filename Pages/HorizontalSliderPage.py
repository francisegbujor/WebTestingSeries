from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class HorizontalSlider(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    slider = (By.CSS_SELECTOR, "input[value='0']")
    slider_number = (By.CSS_SELECTOR, "span[id='range']")

    def __init__(self, driver):
        self.driver = driver

    def open_horizontal_slider_page(self):
        home = HomePage(self.driver)
        return self.click(home.horizontalSliderLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text


from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class FloatingMenu(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    home_link = (By.LINK_TEXT, "Home")

    def __init__(self, driver):
        self.driver = driver

    def open_floating_menu_page(self):
        home = HomePage(self.driver)
        return self.click(home.floatingMenuLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text
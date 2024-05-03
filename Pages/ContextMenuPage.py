from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class ContextMenu(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    display_box = (By.ID, "hot-spot")

    def __init__(self, driver):
        self.driver = driver

    def open_context_menu_page(self):
        home = HomePage(self.driver)
        return self.click(home.contextMenuLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_display_box_element(self):
        return self.find_element(*self.display_box)



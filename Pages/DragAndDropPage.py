from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class DragAndDrop(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    first_column = (By.XPATH, "(//div[@id='column-a'])[1]")
    second_column = (By.XPATH, "(//div[@id='column-b'])[1]")

    def __init__(self, driver):
        self.driver = driver

    def open_drag_and_drop_page(self):
        home = HomePage(self.driver)
        return self.click(home.dragAndDropLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_first_column(self):
        return self.find_element(*self.first_column)

    def get_second_column(self):
        return self.find_element(*self.second_column)
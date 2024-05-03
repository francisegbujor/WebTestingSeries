from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class Dropdown(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    drop_list = (By.ID, "dropdown")

    def __init__(self, driver):
        self.driver = driver

    def open_dropdown_page(self):
        home = HomePage(self.driver)
        return self.click(home.dropDownLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def select_drop_list(self):
        return Select(self.find_element(*self.drop_list))


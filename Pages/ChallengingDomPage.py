from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class ChallengingDom(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    blue_button = (By.CSS_SELECTOR, "[class='button']")
    red_button = (By.CSS_SELECTOR, "[class='button alert']")
    green_button = (By.CSS_SELECTOR, "[class='button success']")
    edit_button0 = (By.LINK_TEXT, "edit")
    delete_button0 = (By.LINK_TEXT, "delete")

    def __init__(self, driver):
        self.driver = driver

    def open_challenging_dom_page(self):
        home = HomePage(self.driver)
        return self.click(home.challengingDOMLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def click_blue_button(self):
        return self.click(self.blue_button)

    def click_red_button(self):
        return self.click(self.red_button)

    def click_green_button(self):
        return self.click(self.green_button)

    def get_edit_button0(self):
        return self.driver.find_element(By.LINK_TEXT, "edit")

    def get_delete_button0(self):
        return self.driver.find_element(By.LINK_TEXT, "delete")
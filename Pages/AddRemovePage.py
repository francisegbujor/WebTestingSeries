from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class AddRemove(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    add_element = (By.XPATH, "(//button[normalize-space()='Add Element'])[1]")
    delete_button = (By.CSS_SELECTOR, ".added-manually")

    def __init__(self, driver):
        self.driver = driver

    def open_add_remove_page(self):
        home = HomePage(self.driver)
        return self.click(home.addRemoveLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def click_add_element(self):
        return self.click(self.add_element)

    def click_delete_button(self):
        return self.click(self.delete_button)

    def get_delete_btn_text(self):
        delete_btn_text = self.get_text(self.delete_button)
        return delete_btn_text




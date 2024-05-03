from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class Checkboxes(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    checkboxes_list = (By.CSS_SELECTOR, "#checkboxes")
    checkbox1 = (By.XPATH, "(//input[@type='checkbox'])[1]")
    checkbox2 = (By.XPATH, "(//input[@type='checkbox'])[2]")

    def __init__(self, driver):
        self.driver = driver

    def open_checkboxes_page(self):
        home = HomePage(self.driver)
        return self.click(home.checkBoxesLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_checkboxes(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "#checkboxes input[type='checkbox']")

    def get_checkbox1(self):
        return self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])[1]")

    def get_checkbox2(self):
        return self.driver.find_element(By.XPATH, "(//input[@type='checkbox'])[2]")

    def click_checkbox1(self):
        return self.click(self.checkbox1)

    def click_checkbox2(self):
        return self.click(self.checkbox2)

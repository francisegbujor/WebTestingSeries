from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class DynamicControls(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h4")
    checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
    remove_button = (By.XPATH, "(//button[normalize-space()='Remove'])[1]")
    add_button = (By.XPATH, "(//button[normalize-space()='Add'])[1]")
    enable_button = (By.XPATH, "(//button[normalize-space()='Enable'])[1]")
    disable_button = (By.XPATH, "(//button[normalize-space()='Disable'])[1]")
    remove_message = (By.ID, "message")
    add_message = (By.ID, "message")
    input_box = (By.CSS_SELECTOR, "input[type='text']")
    enable_message = (By.ID, "message")
    disabled_message = (By.ID, "message")

    def __init__(self, driver):
        self.driver = driver

    def open_dynamic_controls_page(self):
        home = HomePage(self.driver)
        return self.click(home.dynamicControlsLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_checkbox(self):
        return self.find_element(By.CSS_SELECTOR, "input[type='checkbox']")

    def get_remove_button(self):
        return self.find_element(self.remove_button)

    def get_add_button(self):
        return self.find_element(self.add_button)

    def get_disable_button(self):
        return self.find_element(self.disable_button)

    def get_enable_button(self):
        return self.find_element(self.enable_button)

    def get_input_box(self):
        return self.find_element(By.CSS_SELECTOR, "input[type='text']")
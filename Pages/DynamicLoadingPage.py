from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class DynamicLoading(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    example_1 = (By.LINK_TEXT, "Example 1: Element on page that is hidden")
    example_2 = (By.LINK_TEXT, "Example 2: Element rendered after the fact")
    example_1_title = (By.XPATH, "(//h4[normalize-space()='Example 1: Element on page that is hidden'])[1]")
    example1_start_button = (By.XPATH, "(//button[normalize-space()='Start'])[1]")
    example_1_message = (By.CSS_SELECTOR, "div[id='finish']")
    example_2_title = (By.XPATH, "(//h4[normalize-space()='Example 2: Element rendered after the fact'])[1]")
    example2_start_button = (By.XPATH, "(//button[normalize-space()='Start'])[1]")
    example2_message = (By.CSS_SELECTOR, "div[id='finish']")

    def __init__(self, driver):
        self.driver = driver

    def open_dynamic_loading_page(self):
        home = HomePage(self.driver)
        return self.click(home.dynamicLoadingLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text


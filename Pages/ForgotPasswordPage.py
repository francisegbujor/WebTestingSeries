from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class ForgotPassword(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h2")
    email_box = (By.CSS_SELECTOR, "input[name='email']")
    retrieve_password_button = (By.ID, "form_submit")
    email = "demoemail@gmail.com"

    def __init__(self, driver):
        self.driver = driver

    def open_forgot_password_page(self):
        home = HomePage(self.driver)
        return self.click(home.forgotPasswordLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def enter_email_box(self):
        return self.find_element(*self.email_box)

from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class FormAuthentication(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h2")
    username_locator = (By.CSS_SELECTOR, "input[name='username']")
    password_locator = (By.CSS_SELECTOR, "input[name='password']")
    login_button_locator = (By.CSS_SELECTOR, "button[type='submit']")
    username_input = 'tomsmith'
    password_input = 'SuperSecretPassword!'
    login_message_locator = (By.CSS_SELECTOR, "div[id='flash']")
    logout_button_locator = (By.LINK_TEXT, "Logout")
    logout_message_locator = (By.CSS_SELECTOR, "div[id='flash']")

    def __init__(self, driver):
        self.driver = driver

    def open_form_authentication_page(self):
        home = HomePage(self.driver)
        return self.click(home.formAuthenticationLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def enter_username(self):
        return self.find_element(*self.username_locator)

    def enter_password(self):
        return self.find_element(*self.password_locator)

    def get_login_message(self):
        login_text = self.get_text(self.login_message_locator)
        return login_text

    def get_logout_message(self):
        logout_text = self.get_text(self.logout_message_locator)
        return logout_text

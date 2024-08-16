import time

from selenium.webdriver import ActionChains
from Pages.FormAuthenticationPage import FormAuthentication
from utilities.BasePage import BasePage


class TestFormAuthentication(BasePage):

    def test_form_authentication(self):

        log = self.get_logger()
        form_authentication = FormAuthentication(self.driver)

        form_authentication.open_form_authentication_page()
        log.info("Opened Form Authentication Page")

        log.info("Verifying text presence: 'Login Page'")
        form_authentication.verify_text_presence("Login Page")

        title = form_authentication.get_page_title()
        log.info("Page Title: %s", title)
        assert "Login Page" in title, f"Expected 'Login Page' in title, but got '{title}'"

        log.info("Entering username into username box")
        username_box = form_authentication.enter_username()
        ActionChains(self.driver).click(username_box).send_keys(form_authentication.username_input).perform()
        log.info("Entered username successfully")
        username = form_authentication.username_input
        assert "tomsmith" in username, f"Expected 'tomsmith' in username, but got '{username}'"

        log.info("Entering password into password box")
        password_box = form_authentication.enter_password()
        ActionChains(self.driver).click(password_box).send_keys(form_authentication.password_input).perform()
        log.info("Entered password successfully")
        password = form_authentication.password_input
        assert "SuperSecretPassword!" in password, f"Expected 'SuperSecretPassword!' in password, but got '{password}'"

        log.info("Logging in!")
        form_authentication.click(form_authentication.login_button_locator)
        form_authentication.verify_text_presence("You logged into a secure area!")
        log.info("Logged in Successfully!")
        login_message = form_authentication.get_login_message()
        assert "You logged into a secure area!" in login_message, f"Expected 'You logged into a secure area!' in login message, but got '{login_message}'"

        log.info("Logging out!")
        form_authentication.click(form_authentication.logout_button_locator)
        form_authentication.verify_text_presence("You logged out of the secure area!")
        log.info("Logged out Successfully!")
        logout_message = form_authentication.get_logout_message()
        assert "You logged out of the secure area!" in logout_message, f"Expected 'You logged out of the secure area!' in logout message, but got '{logout_message}'"

import time

from selenium.webdriver import ActionChains

from Pages.FileUploadPage import FileUpload
from Pages.ForgotPasswordPage import ForgotPassword
from utilities.BasePage import BasePage


class TestForgotPassword(BasePage):

    def test_forgot_password(self):

        log = self.get_logger()
        forgot_password = ForgotPassword(self.driver)

        forgot_password.open_forgot_password_page()
        log.info("Opened Forgot Password Page")

        forgot_password.verify_text_presence("Forgot Password")
        title = forgot_password.get_page_title()
        log.info("Page Title: %s", title)
        assert "Forgot Password" in title, f"Expected 'Forgot Password' in title, but got '{title}'"

        log.info("Entering email into the email box")
        email_box = forgot_password.enter_email_box()
        ActionChains(self.driver).click(email_box).send_keys(forgot_password.email).perform()
        log.info("Email entered successfully and form is ready")

        forgot_password.click(forgot_password.retrieve_password_button)
        log.info("Password received!")






from utilities.BasePage import BasePage
from Pages.BasicAuthPage import BasicAuth


class TestBasic(BasePage):
    def test_basicauth(self):
        log = self.get_logger()
        basic_auth = BasicAuth(self.driver)
        username = "admin"
        password = "admin"

        basic_auth.open_basic_auth_page(username, password)
        log.info("open basic auth page link")

        basic_auth.verify_text_presence("Basic Auth")
        title = basic_auth.get_page_title()
        log.info("Page Title: %s", title)
        assert "Basic Auth" in title

        valid_message = basic_auth.get_message()
        log.info("Page Message: %s", valid_message)
        assert "Congratulations!" in valid_message

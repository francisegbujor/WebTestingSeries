from utilities.BasePage import BasePage
from Pages.BasicAuthPage import BasicAuth


class TestBasic(BasePage):
    def test_basicauth(self):
        log = self.get_logger()
        basic_auth = BasicAuth(self.driver)
        username = "admin"
        password = "admin"
        basic_auth.open_page(username, password)
        log.info("open page link")
        valid_message = basic_auth.get_message()
        log.info(valid_message)
        assert "Congratulations!" in valid_message

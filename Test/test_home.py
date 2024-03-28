from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class TestHome(BasePage):

    def test_home(self):
        log = self.get_logger()
        home = HomePage(self.driver)
        valid_message = home.get_message()
        log.info(valid_message)
        assert ("Welcome to the-internet" in valid_message)


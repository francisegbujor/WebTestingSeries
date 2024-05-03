from Pages.DigestAuthenticationPage import DigestAuthentication
from utilities.BasePage import BasePage


class TestDigestAuthentication(BasePage):

    def test_digest_authentication(self):

        log = self.get_logger()
        digest_authentication = DigestAuthentication(self.driver)
        username = "admin"
        password = "admin"

        digest_authentication.open_digest_authentication_page(username,password)
        log.info("Opened Digest Authentication Page")

        digest_authentication.verify_text_presence("Digest Auth")
        title = digest_authentication.get_page_title()
        log.info("Page Title: %s", title)
        assert "Digest Auth" in title

        valid_message = digest_authentication.get_message()
        log.info("Page Message: %s", valid_message)
        assert "Congratulations!" in valid_message


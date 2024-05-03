from Pages.ChallengingDomPage import ChallengingDom
from utilities.BasePage import BasePage


class TestChallengingDOM(BasePage):
    def test_challenging_dom(self):
        log = self.get_logger()
        challenging_dom = ChallengingDom(self.driver)

        challenging_dom.open_challenging_dom_page()
        log.info("Opened Challenging DOM Page")

        challenging_dom.verify_text_presence("Challenging DOM")
        title = challenging_dom.get_page_title()
        log.info("page title: %s", title)
        assert "Challenging DOM" in title

        log.info("using while loop to click several buttons to get an expected word")
        blue_word = "qux"
        red_word = "bar"
        green_word = "foo"
        while True:
            challenging_dom.click_blue_button()
            log.info("clicked blue button")
            blue_text = challenging_dom.get_text(challenging_dom.blue_button)
            expected_blue_text = blue_word

            if expected_blue_text == blue_text:
                log.info("Got the correct blue word %s", expected_blue_text)
                break
            else:
                log.info("Expected blue text {} not found in blue button".format(expected_blue_text))

        while True:
            challenging_dom.click_red_button()
            log.info("clicked red button")
            red_text = challenging_dom.get_text(challenging_dom.red_button)
            expected_red_text = red_word

            if expected_red_text == red_text:
                log.info("Got the correct red word %s", expected_red_text)
                break
            else:
                log.info("Expected red text {} not found in green button".format(expected_red_text))

        while True:
            challenging_dom.click_green_button()
            log.info("clicked green button")
            green_text = challenging_dom.get_text(challenging_dom.green_button)
            expected_green_text = green_word

            if expected_green_text == green_text:
                log.info("Got the correct green word %s", expected_green_text)
                break
            else:
                log.info("Expected green text {} not found in green button".format(expected_green_text))

        log.info("Verify if edit button is enabled")
        edit_enabled = challenging_dom.get_edit_button0().is_enabled()
        if edit_enabled:
            log.info("edit button is enabled")
        else:
            log.info("edit button is disabled")

        log.info("Verify if delete button is enabled")
        delete_enabled = challenging_dom.get_delete_button0().is_enabled()
        if delete_enabled:
            log.info("delete button is enabled")
        else:
            log.info("delete button is disabled")



import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder

from Pages.ExitIntentPage import ExitIntent
from utilities.BasePage import BasePage


class TestExitIntent(BasePage):

    def test_exit_intent(self):

        log = self.get_logger()
        exit_intent = ExitIntent(self.driver)

        exit_intent.open_exit_intent_page()
        log.info("Opened Exit Intent Page")

        exit_intent.verify_text_presence("Exit Intent")
        title = exit_intent.get_page_title()
        log.info("Page Title: %s", title)
        assert "Exit Intent" in title

        exit_intent.driver.execute_script("document.querySelector('html').dispatchEvent(new Event('mouseleave'))")
        log.info("Exiting the web page")
        exit_intent.verify_locator_visibility(exit_intent.modal)

        log.info("Modal window appeared on page")
        modal_title = exit_intent.get_modal_title()
        log.info("Modal title: %s", modal_title)
        assert "THIS IS A MODAL WINDOW" in modal_title
        exit_intent.click(exit_intent.close_button)
        log.info("closed modal window")





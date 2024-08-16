import time

from Pages.FloatingMenuPage import FloatingMenu
from utilities.BasePage import BasePage


class TestFloatingMenu(BasePage):

    def test_floating_menu(self):

        log = self.get_logger()
        floating_menu = FloatingMenu(self.driver)

        floating_menu.open_floating_menu_page()
        log.info("Opened Floating Menu Page")

        floating_menu.verify_text_presence("Floating Menu")
        title = floating_menu.get_page_title()
        log.info("Page Title: %s", title)
        assert "Floating Menu" in title

        floating_menu.driver.execute_script("window.scrollTo(0, 500)")
        log.info("scrolling down")
        time.sleep(5)
        assert floating_menu.is_visible(floating_menu.home_link)



import time

import pyautogui
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains

from Pages.ContextMenuPage import ContextMenu
from utilities.BasePage import BasePage


class TestContextMenu(BasePage):

    def test_context_menu(self):
        log = self.get_logger()
        context_menu = ContextMenu(self.driver)

        context_menu.open_context_menu_page()
        log.info("Opened Context Menu Page")

        context_menu.verify_text_presence("Context Menu")
        title = context_menu.get_page_title()
        log.info("Page Title: %s", title)
        assert "Context Menu" in title

        display_box_element = context_menu.get_display_box_element()
        action = ActionChains(self.driver)
        action.context_click(display_box_element).perform()
        log.info("Performed a right click inside display box")

        alert = context_menu.driver.switch_to.alert
        log.info("Switching to pop up alert")
        alert_text = alert.text
        log.info("alert message: %s", alert_text)
        assert "You selected a context menu" in alert_text
        alert.accept()
        log.info("closed pop up alert")

        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        try:
            context_menu.verify_text_not_presence("Context Menu")
            log.info("Element is not present")
        except TimeoutException:
            log.info("Element is present")

        try:
            context_menu.verify_text_presence("Context Menu")
            log.info("Element is present")
        except TimeoutException:
            log.info("Element is not present")



import pyautogui
from selenium.webdriver import ActionChains, Keys

from Pages.DynamicLoadingPage import DynamicLoading
from utilities.BasePage import BasePage


class TestDynamicLoading(BasePage):

    def test_dynamic_loading(self):

        log = self.get_logger()
        dynamic_loading = DynamicLoading(self.driver)

        dynamic_loading.open_dynamic_loading_page()
        log.info("Opened Dynamic Loading Page")

        dynamic_loading.verify_text_presence("Dynamically Loaded Page Elements")
        title = dynamic_loading.get_page_title()
        log.info("Page Title: %s", title)
        assert "Dynamically Loaded Page Elements" in title

        dynamic_loading.click(dynamic_loading.example_1)
        log.info("Opened Example 1 link")
        example1_title = dynamic_loading.get_text(dynamic_loading.example_1_title)
        log.info("Example 1 Title: %s", example1_title)
        assert "Example 1" in example1_title

        dynamic_loading.click(dynamic_loading.example1_start_button)
        log.info("Clicked on start button")
        dynamic_loading.verify_locator_visibility(dynamic_loading.example_1_message)
        example_1_message = dynamic_loading.get_text(dynamic_loading.example_1_message)
        log.info("Example 1 message: %s", example_1_message)
        assert "Hello World!" in example_1_message

        action = ActionChains(self.driver)
        action.context_click().perform()
        pyautogui.press('down')
        pyautogui.press('down')
        pyautogui.press('enter')
        log.info("going back to main page")

        dynamic_loading.verify_locator_visibility(dynamic_loading.example_2)
        dynamic_loading.click(dynamic_loading.example_2)
        log.info("Opened Example 2 link")
        example2_title = dynamic_loading.get_text(dynamic_loading.example_2_title)
        log.info("Example 2 Title: %s", example2_title)
        assert "Example 2" in example2_title

        dynamic_loading.click(dynamic_loading.example2_start_button)
        log.info("Clicked on start button")
        dynamic_loading.verify_locator_visibility(dynamic_loading.example2_message)
        example2_message = dynamic_loading.get_text(dynamic_loading.example2_message)
        log.info("Example 2 message: %s", example2_message)
        assert "Hello World!" in example2_message





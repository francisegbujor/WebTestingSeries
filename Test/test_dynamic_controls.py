from Pages.DynamicControlsPage import DynamicControls
from utilities.BasePage import BasePage


class TestDynamicControls(BasePage):

    def test_dynamic_controls(self):

        log = self.get_logger()
        dynamic_controls = DynamicControls(self.driver)

        dynamic_controls.open_dynamic_controls_page()
        log.info("Opened Dynamic Controls Page")

        dynamic_controls.verify_text_presence("Dynamic Controls")
        title = dynamic_controls.get_page_title()
        log.info("Page Title: %s", title)
        assert "Dynamic Controls" in title

        dynamic_controls.click(dynamic_controls.checkbox)
        log.info("checkbox is clicked")
        assert dynamic_controls.get_checkbox().is_selected(), " Assert False - checkbox is not selected"

        dynamic_controls.click(dynamic_controls.remove_button)
        log.info("Waiting for checkbox to disappear")
        dynamic_controls.verify_locator_invisibility(dynamic_controls.checkbox)
        log.info("Remove button clicked, checkbox is gone")
        remove_message = dynamic_controls.get_text(dynamic_controls.remove_message)
        log.info("Checkbox status: %s", remove_message)
        assert "It's gone!" in remove_message

        dynamic_controls.click(dynamic_controls.add_button)
        log.info("Waiting for checkbox to appear")
        dynamic_controls.verify_locator_visibility(dynamic_controls.checkbox)
        log.info("Add button clicked, checkbox is back")
        add_message = dynamic_controls.get_text(dynamic_controls.add_message)
        log.info("Checkbox status: %s", add_message)
        assert "It's back!" in add_message

        log.info("Input box status: %s", dynamic_controls.get_input_box().is_enabled())
        dynamic_controls.click(dynamic_controls.enable_button)
        log.info("Waiting for input box to be enabled")
        dynamic_controls.verify_locator_visibility(dynamic_controls.enable_message)
        enabled_message = dynamic_controls.get_text(dynamic_controls.enable_message)
        log.info("Input box status: %s", enabled_message)
        assert "It's enabled!" in enabled_message

        log.info("Input box status: %s", dynamic_controls.get_input_box().is_enabled())
        dynamic_controls.click(dynamic_controls.disable_button)
        log.info("Waiting for input box to be disabled")
        dynamic_controls.verify_locator_visibility(dynamic_controls.disabled_message)
        disabled_message = dynamic_controls.get_text(dynamic_controls.disabled_message)
        log.info("Input box status: %s", disabled_message)
        assert "It's disabled!" in disabled_message




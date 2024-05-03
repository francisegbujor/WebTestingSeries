from Pages.CheckboxesPage import Checkboxes
from utilities.BasePage import BasePage


class TestCheckboxes(BasePage):

    def test_checkboxes(self):
        log = self.get_logger()
        checkboxes = Checkboxes(self.driver)

        checkboxes.open_checkboxes_page()
        log.info("Opened Checkboxes Page")

        checkboxes.verify_text_presence("Checkboxes")
        title = checkboxes.get_page_title()
        log.info("page title: %s", title)
        assert "Checkboxes" in title

        log.info("verify if the checkboxes are unexpectedly selected initially")
        list_boxes = checkboxes.get_checkboxes()

        for index, checkbox in enumerate(list_boxes, start=1):
            log.info("Checkbox {} selected status: {}".format(index, checkbox.is_selected()))

        checkboxes.click_checkbox1()
        log.info("Checkbox1 selected status: {}".format(checkboxes.get_checkbox1().is_selected()))
        assert checkboxes.get_checkbox1().is_selected(), "Checkbox1 is selected - Assert Passed"

        checkboxes.click_checkbox2()
        log.info("Checkbox2 selected status: {}".format(checkboxes.get_checkbox2().is_selected()))
        assert not checkboxes.get_checkbox2().is_selected(), "Checkbox2 is not selected - Assert Passed"









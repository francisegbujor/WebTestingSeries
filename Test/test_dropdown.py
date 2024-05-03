from Pages.DropdownPage import Dropdown
from utilities.BasePage import BasePage


class TestDropdown(BasePage):

    def test_dropdown(self):

        log = self.get_logger()
        dropdown = Dropdown(self.driver)

        dropdown.open_dropdown_page()
        log.info("Opened Dropdown Page")

        dropdown.verify_text_presence("Dropdown List")
        title = dropdown.get_page_title()
        log.info("Page Title: %s", title)
        assert "Dropdown List" in title

        select = dropdown.select_drop_list()
        select.select_by_index(2)
        selected_option = select.first_selected_option.text
        log.info("Option selected: %s", selected_option)
        assert "Option 2" in selected_option

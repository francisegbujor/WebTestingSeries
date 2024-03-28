from Pages.AddRemovePage import AddRemove
from utilities.BasePage import BasePage


class TestAddRemove(BasePage):
    def test_add_remove(self):
        log = self.get_logger()
        add_remove = AddRemove(self.driver)

        add_remove.open_add_remove_page()
        log.info("Opened Add/Remove Elements Page")

        add_remove.verify_text_presence("Add/Remove Elements")
        title = add_remove.get_page_title()
        log.info("page title: %s", title)
        assert "Add/Remove Elements" in title

        add_remove.click_add_element()
        log.info("clicked on Add Element button")
        self.verify_text_presence("Delete")
        log.info("wait for delete button to be visible")
        delete_btn = add_remove.get_delete_btn_text()
        log.info("Delete button is visible")
        assert "Delete" in delete_btn

        add_remove.click_delete_button()
        log.info("clicked on Delete button")
        add_remove.verify_locator_invisibility(add_remove.delete_button)
        log.info("Delete button is gone")
        add_remove.assert_element_not_present(add_remove.delete_button)





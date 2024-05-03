from selenium.webdriver import ActionChains

from Pages.DragAndDropPage import DragAndDrop
from utilities.BasePage import BasePage


class TestDragAndDrop(BasePage):

    def test_drag_and_drop(self):

        log = self.get_logger()
        d_and_d = DragAndDrop(self.driver)

        d_and_d.open_drag_and_drop_page()
        log.info("Opened Drag and Drop Page")

        d_and_d.verify_text_presence("Drag and Drop")
        title = d_and_d.get_page_title()
        log.info("Page Title: %s", title)
        assert "Drag and Drop" in title

        actions = ActionChains(self.driver)
        actions.drag_and_drop(d_and_d.get_first_column(), d_and_d.get_second_column()).perform()
        log.info("Dragging column A into second column")
        actions.drag_and_drop(d_and_d.get_second_column(), d_and_d.get_first_column()).perform()
        log.info("Dragging column B into first column")

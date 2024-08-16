from Pages.FramesPage import Frames
from utilities.BasePage import BasePage


class TestFrames(BasePage):

    def test_frames(self):

        log = self.get_logger()
        frames = Frames(self.driver)

        frames.open_frames_page()
        log.info("Opened Frames Page")

        log.info("Verifying text presence: 'Frames'")
        frames.verify_text_presence("Frames")

        title = frames.get_page_title()
        log.info("Page Title: %s", title)
        assert "Frames" in title, f"Expected 'Frames' in title, but got '{title}'"

        frames.click(frames.nested_frames_link)
        log.info("Opened nested frames link")

        self.driver.switch_to.frame("frame-top")
        log.info("Switching to top frame")
        self.driver.switch_to.frame("frame-left")
        log.info("Switching to left frame")
        left_frame_text = frames.get_text_from_left_frame()
        log.info("Left frame text: %s", left_frame_text)

        self.driver.switch_to.default_content()
        log.info("Switching back to default frame")
        self.driver.switch_to.frame("frame-bottom")
        log.info("Switching to bottom frame")
        bottom_frame_text = frames.get_text_from_bottom_frame()
        log.info("Bottom frame text: %s", bottom_frame_text)

        self.driver.switch_to.default_content()
        log.info("Switching back to default frame")




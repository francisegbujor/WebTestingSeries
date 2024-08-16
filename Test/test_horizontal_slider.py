import time

import pyautogui

from Pages.HorizontalSliderPage import HorizontalSlider
from utilities.BasePage import BasePage


class TestHorizontalSlider(BasePage):

    def test_horizontal_slider(self):

        log = self.get_logger()
        horizontal_slider = HorizontalSlider(self.driver)

        horizontal_slider.open_horizontal_slider_page()
        log.info("Opened Horizontal Slider Page")

        log.info("Verifying text presence: 'Horizontal Slider'")
        horizontal_slider.verify_text_presence("Horizontal Slider")

        title = horizontal_slider.get_page_title()
        log.info("Page Title: %s", title)
        assert "Horizontal Slider" in title, f"Expected 'Horizontal Slider' in title, but got '{title}'"

        horizontal_slider.click(horizontal_slider.slider)
        log.info("Clicked on the slider, range is set at 2.5")

        pyautogui.press("right")
        pyautogui.press("right")
        pyautogui.press("right")

        slider_range = horizontal_slider.get_text(horizontal_slider.slider_number)
        log.info(slider_range)
        assert "4" in slider_range, f"Expected '4' in slider_range, but got '{slider_range}'"




import time

from Pages.EntryAdPage import EntryAd
from utilities.BasePage import BasePage


class TestEntryAd(BasePage):

    def test_entry_ad(self):

        log = self.get_logger()
        entry_ad = EntryAd(self.driver)

        entry_ad.open_entry_ad_page()
        log.info("Opened Entry Ad Page")
        time.sleep(3)

        log.info("entry ad appeared on page")
        modal_title = entry_ad.get_window_title()
        log.info("Window title: %s", modal_title)
        assert "THIS IS A MODAL WINDOW" in modal_title
        entry_ad.click(entry_ad.close_button)
        log.info("closed entry ad")

        entry_ad.verify_text_presence("Entry Ad")
        title = entry_ad.get_page_title()
        log.info("Page Title: %s", title)
        assert "Entry Ad" in title

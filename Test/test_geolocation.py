import time

from Pages.GeolocationPage import Geolocation
from utilities.BasePage import BasePage


class TestGeolocation(BasePage):

    def test_geolocation(self):

        log = self.get_logger()
        geolocation = Geolocation(self.driver)

        geolocation.open_geolocation_page()
        log.info("Opened Geolocation Page")

        log.info("Verifying text presence: 'Geolocation'")
        geolocation.verify_text_presence("Geolocation")

        title = geolocation.get_page_title()
        log.info("Page Title: %s", title)
        assert "Geolocation" in title, f"Expected 'Geolocation' in title, but got '{title}'"

        geolocation.click(geolocation.location_button)
        log.info("Getting current location")

        geolocation.verify_text_presence("Latitude:")
        log.info("Location loaded")
        time.sleep(1)
        latitude = geolocation.get_latitude()
        longitude = geolocation.get_longitude()
        log.info(f"Latitude is: '{latitude}', Longitude is: '{longitude}'")

        geolocation.click(geolocation.google_location_link)
        time.sleep(5)

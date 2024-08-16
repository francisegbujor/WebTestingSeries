from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class Geolocation(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    location_button = (By.CSS_SELECTOR, "button[onclick='getLocation()']")
    latitude_locator = (By.ID, "lat-value")
    longitude_locator = (By.ID, "long-value")
    google_location_link = (By.LINK_TEXT, "See it on Google")

    def __init__(self, driver):
        self.driver = driver

    def open_geolocation_page(self):
        home = HomePage(self.driver)
        return self.click(home.geolocationLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_latitude(self):
        latitude_text = self.get_text(self.latitude_locator)
        return latitude_text

    def get_longitude(self):
        longitude_text = self.get_text(self.longitude_locator)
        return longitude_text
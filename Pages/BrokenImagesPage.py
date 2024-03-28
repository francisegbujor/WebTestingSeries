from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage
import requests


class BrokenImages(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    image_list = (By.TAG_NAME, "img")
    brokenImageCount = 0
    properImageCount = 0

    def __init__(self, driver):
        self.driver = driver

    def open_broken_image_page(self):
        home = HomePage(self.driver)
        return self.click(home.brokenImagesLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_image_total(self):
        image_elements = self.finds(*self.image_list)
        return len(image_elements)

    def get_images_broken(self):
        broken_images = []
        image_elements = self.finds(*self.image_list)
        for img in image_elements:
            try:
                src = img.get_attribute('src')
                if src:
                    response = requests.head(src)
                    if response.status_code != 200:
                        broken_images.append((img.get_attribute('outerHTML'), response))
                        self.brokenImageCount += 1
                else:
                    print("Image source attribute is missing")
            except requests.exceptions.RequestException as e:
                print(f"Error checking image with src {src}: {e}")
        return broken_images

    def get_images_proper(self):
        proper_images = []
        image_elements = self.finds(*self.image_list)
        for img in image_elements:
            try:
                src = img.get_attribute('src')
                if src:
                    response = requests.head(src)
                    if response.status_code == 200:
                        proper_images.append((img.get_attribute('outerHTML'), response))
                        self.properImageCount += 1
                else:
                    print("Image source attribute is missing")
            except requests.exceptions.RequestException as e:
                print(f"Error checking image with src {src}: {e}")
        return proper_images




from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage
import requests


class DynamicContent(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    image_list = (By.TAG_NAME, "img")
    static_content_button = (By.LINK_TEXT, "click here")

    def __init__(self, driver):
        self.driver = driver

    def open_dynamic_content_page(self):
        home = HomePage(self.driver)
        return self.click(home.dynamicContentLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

    def get_images(self):
        images = []
        image_element = self.find_elements(*self.image_list)
        for img in image_element:
            try:
                src = img.get_attribute('src')
                if src:
                    response = requests.head(src)
                    if response.status_code == 200:
                        images.append((img.get_attribute('outerHTML'), response))
                else:
                    print("Image source attribute is missing")
            except requests.exceptions.RequestException as e:
                print(f"Error checking image with src {src}: {e}")
        return images

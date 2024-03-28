from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class HomePage(BasePage):
    message = (By.CSS_SELECTOR, ".heading")
    addRemoveLink = (By.LINK_TEXT, "Add/Remove Elements")
    basicAuthLink = (By.LINK_TEXT, "Basic Auth")
    brokenImagesLink = (By.LINK_TEXT, "Broken Images")

    def __init__(self, driver):
        self.driver = driver

    def get_message(self):
        message_text = self.get_text(self.message)
        return message_text

    def click_add_remove(self):
        return self.driver.find_element(*HomePage.addRemoveLink)

    # basic auth link doesn't get clicked. user and pass in given directly into URL
    def get_basic_auth(self):
        return self.driver.find_element(*HomePage.basicAuthLink)

    def click_broken_images(self):
        return self.driver.find_element(*HomePage.brokenImagesLink)

from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class FileUpload(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    choose_file_button = (By.CSS_SELECTOR, "form[method='POST']")
    choose = (By.CSS_SELECTOR, "input[name='file']")
    upload_button = (By.ID, "file-submit")

    def __init__(self, driver):
        self.driver = driver

    def open_file_download_page(self):
        home = HomePage(self.driver)
        return self.click(home.fileUploadLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text

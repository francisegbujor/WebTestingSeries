from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class FileDownload(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    testing_pdf_link = (By.LINK_TEXT, "testing.pdf")
    testing_pdf_filepath = ("C:\\Users\\Francis\\Downloads\\testing.pdf")

    def __init__(self, driver):
        self.driver = driver

    def open_file_download_page(self):
        home = HomePage(self.driver)
        return self.click(home.fileDownloadLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text
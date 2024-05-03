from selenium.webdriver.common.by import By

from Pages.HomePage import HomePage
from utilities.BasePage import BasePage


class DisappearingElements(BasePage):

    page_title = (By.CSS_SELECTOR, "div[id='content'] h3")
    home_tab = (By.LINK_TEXT, "Home")
    about_tab = (By.LINK_TEXT, "About")
    contact_us_tab = (By.LINK_TEXT, "Contact Us")
    portfolio_tab = (By.LINK_TEXT, "Portfolio")
    gallery_tab = (By.LINK_TEXT, "Gallery")

    def __init__(self, driver):
        self.driver = driver

    def open_disappearing_elements_page(self):
        home = HomePage(self.driver)
        return self.click(home.disappearingElementsLink)

    def get_page_title(self):
        title_text = self.get_text(self.page_title)
        return title_text


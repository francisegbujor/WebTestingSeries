from selenium.webdriver.common.by import By

from utilities.BasePage import BasePage


class HomePage(BasePage):
    message = (By.CSS_SELECTOR, ".heading")
    addRemoveLink = (By.LINK_TEXT, "Add/Remove Elements")
    basicAuthLink = (By.LINK_TEXT, "Basic Auth")
    brokenImagesLink = (By.LINK_TEXT, "Broken Images")
    challengingDOMLink = (By.LINK_TEXT, "Challenging DOM")
    checkBoxesLink = (By.LINK_TEXT, "Checkboxes")
    contextMenuLink = (By.LINK_TEXT, "Context Menu")
    digestAuthenticationLink = (By.LINK_TEXT, "Digest Authentication")
    disappearingElementsLink = (By.LINK_TEXT, "Disappearing Elements")
    dragAndDropLink = (By.LINK_TEXT, "Drag and Drop")
    dropDownLink = (By.LINK_TEXT, "Dropdown")
    dynamicContentLink = (By.LINK_TEXT, "Dynamic Content")
    dynamicControlsLink = (By.LINK_TEXT, "Dynamic Controls")
    dynamicLoadingLink = (By.LINK_TEXT, "Dynamic Loading")
    entryAdLink = (By.LINK_TEXT, "Entry Ad")
    exitIntentLink = (By.LINK_TEXT, "Exit Intent")
    fileDownloadLink = (By.LINK_TEXT, "File Download")
    fileUploadLink = (By.LINK_TEXT, "File Upload")
    floatingMenuLink = (By.LINK_TEXT, "Floating Menu")
    forgotPasswordLink = (By.LINK_TEXT, "Forgot Password")
    formAuthenticationLink = (By.LINK_TEXT, "Form Authentication")
    framesLink = (By.LINK_TEXT, "Frames")
    geolocationLink = (By.LINK_TEXT, "Geolocation")
    horizontalSliderLink = (By.LINK_TEXT, "Horizontal Slider")

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

    def click_challenging_dom(self):
        return self.driver.find_element(*HomePage.challengingDOMLink)

    def click_checkboxes(self):
        return self.driver.find_element(*HomePage.checkBoxesLink)

    def click_context_menu(self):
        return self.driver.find_element(*HomePage.contextMenuLink)

    def click_digest_authentication(self):
        return self.driver.find_element(*HomePage.digestAuthenticationLink)

    def click_disappearing_elements(self):
        return self.driver.find_element(*HomePage.disappearingElementsLink)

    def click_drag_and_drop(self):
        return self.driver.find_element(*HomePage.dragAndDropLink)

    def click_dropdown(self):
        return self.driver.find_element(*HomePage.dropDownLink)

    def click_dynamic_content(self):
        return self.driver.find_element(*HomePage.dynamicContentLink)

    def click_dynamic_controls(self):
        return self.driver.find_element(*HomePage.dynamicControlsLink)
    
    def click_dynamic_loading(self):
        return self.driver.find_element(*HomePage.dynamicLoadingLink)

    def click_entry_ad(self):
        return self.driver.find_element(*HomePage.entryAdLink)

    def click_exit_intent(self):
        return self.driver.find_element(*HomePage.exitIntentLink)

    def click_file_download(self):
        return self.driver.find_element(*HomePage.fileDownloadLink)

    def click_file_upload(self):
        return self.driver.find_element(*HomePage.fileUploadLink)

    def click_floating_menu(self):
        return self.driver.find_element(*HomePage.floatingMenuLink)

    def click_forgot_password(self):
        return self.driver.find_element(*HomePage.forgotPasswordLink)

    def click_form_authentication(self):
        return self.driver.find_element(*HomePage.formAuthenticationLink)

    def click_frames(self):
        return self.driver.find_element(*HomePage.framesLink)

    def click_geolocation(self):
        return self.driver.find_element(*HomePage.geolocationLink)

    def click_horizontal_slider(self):
        return self.driver.find_element(*HomePage.horizontalSliderLink)
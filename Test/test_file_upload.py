from Pages.FileUploadPage import FileUpload
from utilities.BasePage import BasePage


class TestFileUpload(BasePage):

    def test_file_upload(self):

        log = self.get_logger()
        file_upload = FileUpload(self.driver)

        file_upload.open_file_download_page()
        log.info("Opened File Upload Page")

        log.info("Verifying text presence: 'File Uploader'")
        file_upload.verify_text_presence("File Uploader")

        title = file_upload.get_page_title()
        log.info("Page Title: %s", title)
        assert "File Uploader" in title, f"Expected 'File Uploader' in title, but got '{title}'"

        log.info("Clicking choose file button")
        file_upload.click(file_upload.choose_file_button)

        file_upload.click(file_upload.choose)

        log.info("Verifying choose file button is present")
        file_upload.assert_element_present(file_upload.choose_file_button)

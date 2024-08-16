import os
import time

from Pages.FileDownloadPage import FileDownload
from utilities.BasePage import BasePage


class TestFileDownload(BasePage):

    def test_file_download(self):

        log = self.get_logger()
        file_download = FileDownload(self.driver)

        file_download.open_file_download_page()
        log.info("Opened File Download Page")

        file_download.verify_text_presence("File Downloader")
        title = file_download.get_page_title()
        log.info("Page Title: %s", title)
        assert "File Downloader" in title

        if os.path.exists(file_download.testing_pdf_filepath):
            log.info("file path already exists")
            os.remove(file_download.testing_pdf_filepath)
            log.info("previous testing.pdf file download is removed")

        file_download.click(file_download.testing_pdf_link)
        time.sleep(3)
        log.info("testing.pdf file is downloaded")
        if os.path.exists(file_download.testing_pdf_filepath):
            log.info("file path is valid")
            assert True
        else:
            log.error("File download failed or file not found.")
            assert False, "File download failed."

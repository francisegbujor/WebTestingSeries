from Pages.BrokenImagesPage import BrokenImages
from utilities.BasePage import BasePage


class TestBrokenImages(BasePage):
    def test_broken_image(self):
        log = self.get_logger()
        broken_image = BrokenImages(self.driver)

        broken_image.open_broken_image_page()
        log.info("Opened Broken Images Page")

        broken_image.verify_text_presence("Broken Images")
        title = broken_image.get_page_title()
        log.info("page title: %s", title)
        assert "Broken Images" in title

        total_image = broken_image.get_image_total()
        log.info('Total number of images: %s', total_image)

        broken_image_info = broken_image.get_images_broken()
        log.info("get broken images info: %s", broken_image_info)
        broken_image_count_total = broken_image.brokenImageCount
        log.info('This page has ' + str(broken_image_count_total) + ' broken images')
        for _, response in broken_image_info:
            assert response.status_code == 404
        assert broken_image_count_total == len(broken_image_info)

        proper_image_info = broken_image.get_images_proper()
        log.info("get proper images info: %s", proper_image_info)
        proper_image_count_total = broken_image.properImageCount
        log.info('This page has ' + str(proper_image_count_total) + ' proper images')
        for _, response in proper_image_info:
            assert response.status_code == 200
        assert proper_image_count_total == len(proper_image_info)





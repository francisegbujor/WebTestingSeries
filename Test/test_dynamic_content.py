from Pages.DynamicContentPage import DynamicContent
from utilities.BasePage import BasePage


class TestDynamicContent(BasePage):

    def test_dynamic_content(self):

        log = self.get_logger()
        dynamic_content = DynamicContent(self.driver)

        dynamic_content.open_dynamic_content_page()
        log.info("Opened Dynamic Content Page")

        dynamic_content.verify_text_presence("Dynamic Content")
        title = dynamic_content.get_page_title()
        log.info("Page Title: %s", title)
        assert "Dynamic Content" in title

        images_list1_info = dynamic_content.get_images()
        log.info("get images list 1 info: %s", images_list1_info)

        dynamic_content.click(dynamic_content.static_content_button)
        log.info("refreshed the page and made some content static")

        images_list2_info = dynamic_content.get_images()
        log.info("get images list 2 info: %s", images_list2_info)

        dynamic_content.click(dynamic_content.static_content_button)
        log.info("refreshed the paged again")

        images_list3_info = dynamic_content.get_images()
        log.info("get images list 3 info: %s", images_list3_info)

        list2_image2_src = ""
        for index, image in enumerate(images_list2_info):
            if index == 1:
                list2_image2_src = image[0]
                break
        log.info("list2_image2 src: %s", list2_image2_src)

        list3_image2_src = ""
        for index, image in enumerate(images_list3_info):
            if index == 1:
                list3_image2_src = image[0]
                break
        log.info("list3_image2 src: %s", list3_image2_src)
        assert list2_image2_src == list3_image2_src
        log.info("images are the same")

        list2_image3_src = ""
        for index, image in enumerate(images_list2_info):
            if index == 2:
                list2_image3_src = image[0]
                break
        log.info("list2_image3 src: %s", list2_image3_src)

        list3_image3_src = ""
        for index, image in enumerate(images_list3_info):
            if index == 2:
                list3_image3_src = image[0]
                break
        log.info("list3_image3 src: %s", list3_image3_src)
        assert list2_image3_src == list3_image3_src
        log.info("images are the same")






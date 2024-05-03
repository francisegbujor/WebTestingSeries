from Pages.DisappearingElementsPage import DisappearingElements
from utilities.BasePage import BasePage


class TestDisappearingElements(BasePage):

    def test_disappearing_elements(self):

        log = self.get_logger()
        disappearing_elements = DisappearingElements(self.driver)

        disappearing_elements.open_disappearing_elements_page()
        log.info("Opened Disappearing Elements Page")

        disappearing_elements.verify_text_presence("Disappearing Elements")
        title = disappearing_elements.get_page_title()
        log.info("Page Title: %s", title)
        assert "Disappearing Elements" in title

        if disappearing_elements.is_visible(disappearing_elements.home_tab):
            log.info("Home tab is visible")
        else:
            log.info("Home tab is not visible")
        home_link = disappearing_elements.get_text(disappearing_elements.home_tab)
        log.info("Tab: %s", home_link)
        assert "Home" in home_link

        if disappearing_elements.is_visible(disappearing_elements.about_tab):
            log.info("About tab is visible")
        else:
            log.info("About tab is not visible")
        about_link = disappearing_elements.get_text(disappearing_elements.about_tab)
        log.info("Tab: %s", about_link)
        assert "About" in about_link

        if disappearing_elements.is_visible(disappearing_elements.contact_us_tab):
            log.info("Contact Us tab is visible")
        else:
            log.info("Contact Us is not visible")
        contact_us_link = disappearing_elements.get_text(disappearing_elements.contact_us_tab)
        log.info("Tab: %s", contact_us_link)
        assert "Contact Us" in contact_us_link

        if disappearing_elements.is_visible(disappearing_elements.portfolio_tab):
            log.info("Portfolio tab is visible")
        else:
            log.info("Portfolio tab is not visible")
        portfolio_tab_link = disappearing_elements.get_text(disappearing_elements.portfolio_tab)
        log.info("Tab: %s", portfolio_tab_link)
        assert "Portfolio" in portfolio_tab_link

        if disappearing_elements.is_visible(disappearing_elements.gallery_tab):
            log.info("Gallery tab is visible")
            gallery_link = disappearing_elements.get_text(disappearing_elements.gallery_tab)
            log.info("Tab: %s", gallery_link)
            assert "Gallery" in gallery_link
        else:
            log.info("Gallery tab is not visible")







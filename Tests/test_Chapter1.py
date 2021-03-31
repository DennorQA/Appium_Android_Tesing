from Settings.Config import Config
from PageObject.MainPage import MainPage
import pytest


class Test_Chapter1:

    @pytest.mark.usefixtures('init_driver')
    def test_chapters_are_displayed(self):
        main_page = MainPage(self.driver)
        list_of_chapters = main_page.get_list_of_elements(Config.ELEMENTS)

        assert len(list_of_chapters) == 11
        assert list_of_chapters == Config.EXPECTED_CHAPTER_LIST

    @pytest.mark.usefixtures('init_driver')
    def test_chapter1_is_displayed(self):
        main_page = MainPage(self.driver)
        is_displayed = main_page.is_displayed(main_page.chapter1_field)

        assert is_displayed == True

    @pytest.mark.usefixtures('init_driver')
    def test_basic_text_view_is_displayed(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter1(main_page.chapter1_field)
        is_displayed = main_page.is_displayed(main_page.basic_text_view_field)

        assert is_displayed == True

    @pytest.mark.usefixtures('init_driver')
    def test_second_text_view_is_displayed(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter1(main_page.chapter1_field)
        main_page.tap_basic_text_view(main_page.basic_text_view_field)
        actual_text = main_page.get_element_text(main_page.second_text_view_field)

        assert actual_text == Config.EXPECTED_SECOND_VIEW_TEXT
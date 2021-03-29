from appium import webdriver
from Settings.Config import Config
from PageObject.MainPage import MainPage
from Tests.init_test import init_test


class Test_Chapter1:

    def test_chapters_are_displayed(self):
        main_page = MainPage(init_test.setup_driver(self))
        list_of_chapters = main_page.get_list_of_elements(Config.ELEMENTS)

        assert len(list_of_chapters) == 11
        assert list_of_chapters == Config.EXPECTED_CHAPTER_LIST
        init_test.tear_down(self)

    def test_chapter1_is_displayed(self):
        main_page = MainPage(init_test.setup_driver(self))
        is_displayed = main_page.is_displayed(main_page.chapter1_field)

        assert is_displayed == True
        init_test.tear_down(self)

    def test_basic_text_view_is_displayed(self):
        main_page = MainPage(init_test.setup_driver(self))
        main_page.tap_chapter1(main_page.chapter1_field)
        is_displayed = main_page.is_displayed(main_page.basic_text_view_field)

        assert is_displayed == True
        init_test.tear_down(self)

    def test_second_text_view_is_displayed(self):
        main_page = MainPage(init_test.setup_driver(self))
        main_page.tap_chapter1(main_page.chapter1_field)
        main_page.tap_basic_text_view(main_page.basic_text_view_field)
        actual_text = main_page.get_element_text(main_page.second_text_view_field)

        assert actual_text == Config.EXPECTED_SECOND_VIEW_TEXT
        init_test.tear_down(self)
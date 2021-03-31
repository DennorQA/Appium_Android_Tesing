from Settings.Config import Config
from PageObject.MainPage import MainPage
import pytest


class Test_Chapter3:

    @pytest.mark.usefixtures('init_driver')
    def test_chapter3_is_displayed(self):
        main_page = MainPage(self.driver)
        is_displayed = main_page.is_displayed(main_page.chapter3_field)

        assert is_displayed == True

    @pytest.mark.usefixtures('init_driver')
    def test_basic_view_is_displayed(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter3(main_page.chapter3_field)
        is_displayed = main_page.is_displayed(main_page.basic_view_field)

        assert is_displayed == True

    @pytest.mark.usefixtures('init_driver')
    def test_basic_view_activity_title_is_displayed(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter3(main_page.chapter3_field)
        main_page.tap_basic_view(main_page.basic_view_field)
        actual_text = main_page.get_element_text(main_page.basic_view_activity_title)

        assert actual_text == "BasicViewsActivity"

    @pytest.mark.usefixtures('init_driver')
    def test_button_is_displayed(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter3(main_page.chapter3_field)
        main_page.tap_basic_view(main_page.basic_view_field)
        is_displayed = main_page.is_displayed(main_page.button_field)
        actual_text = main_page.get_element_text(main_page.button_field)

        assert is_displayed == True
        assert actual_text == "Button"

    @pytest.mark.usefixtures('init_driver')
    def test_simple_list_view_is_displayed(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter3(main_page.chapter3_field)
        is_displayed = main_page.is_displayed(main_page.simple_list_view_field)

        assert is_displayed == True

    @pytest.mark.usefixtures('init_driver')
    def test_list_of_elements_is_displayed(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter3(main_page.chapter3_field)
        main_page.tap_simple_list_view(main_page.simple_list_view_field)
        list_of_elements = main_page.get_list_of_elements(Config.ELEMENTS)

        assert len(list_of_elements) == 4
        assert list_of_elements == Config.EXPECTED_SIMPLE_VIEW_LIST

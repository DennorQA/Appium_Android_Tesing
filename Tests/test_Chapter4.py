from Settings.Config import Config
from PageObject.MainPage import MainPage
import pytest


class Test_Chapter4:

    @pytest.mark.usefixtures('init_driver')
    def test_xml_button_functionality_in_click_handlers(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter4(main_page.chapter4_field)
        main_page.tap_basic_click_handlers(main_page.basic_click_handlers_field)
        main_page.tap_xml_on_click_button(main_page.xml_on_click_button_field)
        actual_text1 = main_page.get_element_text(main_page.xml_java_clicked_text_field)
        main_page.tap_xml_java_ok_button(main_page.xml_java_ok_button_field)
        actual_text2 = main_page.get_element_text(main_page.main_menu_java_xml_text_field)

        assert actual_text1 == Config.EXPECTED_XML_TEXT
        assert actual_text2 == Config.INPUT_TEXT

    @pytest.mark.usefixtures('init_driver')
    def test_java_button_functionality_in_click_handlers(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter4(main_page.chapter4_field)
        main_page.tap_basic_click_handlers(main_page.basic_click_handlers_field)
        main_page.tap_java_on_click_button(main_page.java_on_click_button_field)
        actual_text1 = main_page.get_element_text(main_page.xml_java_clicked_text_field)
        main_page.tap_xml_java_ok_button(main_page.xml_java_ok_button_field)
        actual_text2 = main_page.get_element_text(main_page.main_menu_java_xml_text_field)

        assert actual_text1 == Config.EXPECTED_JAVA_TEXT
        assert actual_text2 == Config.INPUT_TEXT
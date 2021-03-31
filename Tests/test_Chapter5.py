from Settings.Config import Config
from PageObject.MainPage import MainPage
import pytest


class Test_Chapter5:

    @pytest.mark.usefixtures('init_driver')
    def test_intent_with_results_text_is_displayed(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter5(main_page.chapter5_field)
        main_page.tap_intent_with_results(main_page.intent_with_results_field)
        main_page.tap_launch_activity_for_result(main_page.launch_activity_for_result_field)
        main_page.send_keys(main_page.text_input_field, Config.INPUT_TEXT)
        main_page.tap_send_result(main_page.send_result_button_field)
        actual_text = main_page.get_element_text(main_page.result_field)

        assert actual_text == Config.INPUT_TEXT

    @pytest.mark.usefixtures('init_driver')
    def test_implicit_intents_url_is_displayed(self):
        main_page = MainPage(self.driver)
        main_page.tap_chapter5(main_page.chapter5_field)
        main_page.tap_implicit_intents(main_page.implicit_intent_field)
        main_page.send_keys(main_page.input_url_field, Config.INPUT_URL)
        main_page.tap_visit_button(main_page.visit_button_field)
        actual_title = main_page.get_element_text(main_page.salesforce_image)

        assert actual_title == Config.EXPECTED_TEXT
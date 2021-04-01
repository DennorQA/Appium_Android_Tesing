from PageObject.BasePage import BasePage
from selenium.webdriver.common.by import By
from Settings.Config import Config


class MainPage(BasePage):

    chapter1_field = (By.XPATH, Config.GENERAL_PATH + "TextView[1]")
    chapter2_field = (By.XPATH, Config.GENERAL_PATH + "TextView[2]")
    chapter3_field = (By.XPATH, Config.GENERAL_PATH + "TextView[3]")
    chapter4_field = (By.XPATH, Config.GENERAL_PATH + "TextView[4]")
    chapter5_field = (By.XPATH, Config.GENERAL_PATH + "TextView[5]")
    chapter6_field = (By.XPATH, Config.GENERAL_PATH + "TextView[6]")
    chapter7_field = (By.XPATH, Config.GENERAL_PATH + "TextView[7]")
    chapter8_field = (By.XPATH, Config.GENERAL_PATH + "TextView[8]")
    chapter9_field = (By.XPATH, Config.GENERAL_PATH + "TextView[9]")
    chapter10_field = (By.XPATH, Config.GENERAL_PATH + "TextView[10]")
    basic_text_view_field = (By.XPATH, Config.GENERAL_PATH + "TextView[2]")
    basic_view_field = (By.XPATH, Config.GENERAL_PATH + "TextView[5]")
    simple_list_view_field = (By.XPATH, Config.GENERAL_PATH + "TextView[7]")
    intent_with_results_field = (By.XPATH, Config.GENERAL_PATH + "TextView[8]")
    implicit_intent_field = (By.XPATH, Config.GENERAL_PATH + "TextView[7]")
    basic_click_handlers_field = (By.XPATH, Config.GENERAL_PATH + "TextView[5]")
    handling_list_view_clicks = (By.XPATH, Config.GENERAL_PATH + "TextView[6]")
    xml_on_click_button_field = (By.XPATH, Config.GENERAL_PATH + "LinearLayout/android.widget.Button[1]")
    java_on_click_button_field = (By.ID, "codepath.apps.demointroandroid:id/btnClick2")
    xml_java_clicked_text_field = (By.ID, "android:id/message")
    xml_java_ok_button_field = (By.ID, "android:id/button1")
    main_menu_java_xml_text_field = (By.ID, "codepath.apps.demointroandroid:id/textView1")
    salesforce_image = (By.XPATH, "//android.view.View[@content-desc=\"Salesforce\"]/android.widget.Image")
    input_url_field = (By.ID, "codepath.apps.demointroandroid:id/txtUrlAddress")
    visit_button_field = (By.ID, "codepath.apps.demointroandroid:id/button1")
    result_field = (By.ID, "codepath.apps.demointroandroid:id/txtDisplayResult")
    send_result_button_field = (By.ID, "codepath.apps.demointroandroid:id/btnSubmit")
    text_input_field = (By.ID, "codepath.apps.demointroandroid:id/txtRandomResultText")
    launch_activity_for_result_field = (By.ID, "codepath.apps.demointroandroid:id/button1")
    basic_view_activity_title = (By.ID, "android:id/action_bar_title")
    second_text_view_field = (By.XPATH, Config.GENERAL_PATH + "RelativeLayout/android.widget.TextView")
    button_field = (By.ID, "codepath.apps.demointroandroid:id/button1")
    list_view = (By.ID, "codepath.apps.demointroandroid:id/lvDemo")
    list_of_chapters = (By.ID, "codepath.apps.demointroandroid:id/elvChapters")
    chapters = (By.CLASS_NAME, "android.widget.TextView")

    def __init__(self, driver):
        super().__init__(driver)

    def tap_chapter1(self, chapter1_field):
        self.tap(chapter1_field)

    def tap_chapter3(self, chapter3_field):
        self.tap(chapter3_field)

    def tap_chapter4(self, chapter4_field):
        self.tap(chapter4_field)

    def tap_chapter5(self, tap_chapter5):
        self.tap(tap_chapter5)

    def tap_intent_with_results(self, intent_with_results):
        self.tap(intent_with_results)

    def tap_basic_text_view(self, basic_text_view_field):
        self.tap(basic_text_view_field)

    def tap_basic_view(self, basic_view_field):
        self.tap(basic_view_field)

    def tap_simple_list_view(self, simple_list_view_field):
        self.tap(simple_list_view_field)

    def tap_launch_activity_for_result(self, launch_activity_for_result_field):
        self.tap(launch_activity_for_result_field)

    def tap_implicit_intents(self, implicit_intent_field):
        self.tap(implicit_intent_field)

    def tap_send_result(self, send_result_button_field):
        self.tap(send_result_button_field)

    def tap_visit_button(self, visit_button_field):
        self.tap(visit_button_field)

    def tap_basic_click_handlers(self, basic_click_handlers_field):
        self.tap(basic_click_handlers_field)

    def tap_xml_on_click_button(self, xml_on_click_button_field):
        self.tap(xml_on_click_button_field)

    def tap_java_on_click_button(self, java_on_click_button_field):
        self.tap(java_on_click_button_field)

    def tap_xml_java_ok_button(self, xml_java_ok_button_field):
        self.tap(xml_java_ok_button_field)

    def tap_handling_list_view_clicks(self, second_text_view_field):
        self.tap(second_text_view_field)

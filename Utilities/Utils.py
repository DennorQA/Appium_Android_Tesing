
class Utils:

    @staticmethod
    def open_chapter(driver, by_class_locator, chapter_name):
        chapter_list = driver.find_elements_by_class_name(by_class_locator)
        for element in chapter_list:
            if element == chapter_name:
                element.click()

from selenium.webdriver.common.by import By


class SeacrhBase:


    def elements_by_tag_name(self, tag_name):
        return By.TAG_NAME, tag_name


    def elements_by_class_name(self, class_name):
        return By.CLASS_NAME, class_name

    def elements_by_link_text(self, link_text):
        return By.LINK_TEXT, link_text


    def elements_by_id(self, id):
        return By.ID, id
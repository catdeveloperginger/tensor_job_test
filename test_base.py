import pytest
from app_helper import AppHelper
from elements_helper import ElementsHelper


@pytest.mark.usefixtures("get_driver")
class TestBase(AppHelper):
    def go_to_contacts(self):
        self.go_to_site('https://sbis.ru/')
        elements = self.find_element(class_name='sbisru-Header__menu-item')
        find_el = ElementsHelper(elements).find_el_for_tag_and_text('контакты', 'a')
        self.click_link(find_el)











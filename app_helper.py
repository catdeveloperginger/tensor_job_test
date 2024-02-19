from selenium.webdriver import ActionChains

from app_base import AppBase
from config import *


class AppHelper(AppBase):

    def find_link(self, link):
        el = self.find_element(tag_name='a')
        for i in el:
            href = i.get_attribute('href')
            if href:
                if link in href:
                    return i




    def find_and_click(self, **kwargs):
        for k, v in kwargs.items():
            match k:
                case 'link':
                    el = self.find_link(v)
                    assert el, message_no_element_found
                    el.click()

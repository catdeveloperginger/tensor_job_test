import time

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from elements_helper import ElementsHelper
from search_base import SeacrhBase
from config import *




@pytest.mark.usefixtures("get_driver")
class AppBase:

    search = SeacrhBase()


    def go_to_site(self, url):
        self.main_window = self.driver.current_window_handle
        self.driver.get(url)


    def close_tab(self):
        all_windows = self.driver.window_handles
        all_windows.remove(self.main_window)

        for window in all_windows:
            self.driver.switch_to.window(window)
            self.driver.close()

        self.driver.switch_to.window(self.main_window)

    def switch_tab(self, title_page):
        window_handles = self.driver.window_handles


        new_window_handle = None
        for handle in window_handles:
            self.driver.switch_to.window(handle)
            if title_page.lower() in self.driver.title.lower():
                new_window_handle = handle
                break
        if new_window_handle:
            self.driver.switch_to.window(new_window_handle)
            return True


    def check_current_url(self, url):
        if self.driver.current_url == url:
            return True

    def find_element(self, **kwargs):
        for k, v in kwargs.items():
            match k:
                case 'tag_name':
                    return WebDriverWait(self.driver, time_for_search).until(EC.presence_of_all_elements_located((self.search.elements_by_tag_name(v))))
                case 'class_name':
                    return WebDriverWait(self.driver, time_for_search).until(EC.presence_of_all_elements_located((self.search.elements_by_class_name(v))))
                case 'link_text':
                    return WebDriverWait(self.driver, time_for_search).until(EC.presence_of_all_elements_located((self.search.elements_by_link_text(v))))
                case 'id':
                    return WebDriverWait(self.driver, time_for_search).until(
                        EC.presence_of_all_elements_located((self.search.elements_by_id(v))))

    def scroll_element(self, element: WebElement):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_img_link(self, alt_text: str, list_links: WebElement) -> bool:
        """
                        Clicks on a picture with a link, finds the desired element through the parameter 'alt'
                        :param alt_text: alt text <img> tag.
                        :param list_links: Elements finds webdriver.
                        """

        for el in list_links:
            a = ElementsHelper(el).filter_tag('img')
            for i in a:
                if alt_text.lower() ==i.get_attribute('alt').lower():
                    self.go_to_site(el.get_attribute('href').lower())
                    return True


    def click_link(self, element: WebElement) -> None:

        """
                        Clicks on the link. Accepts an element containing an <a> tag.
                        Mouse hover is simulated
                        :param element: page element that contains the desired link
                        """

        
        self.actions.move_to_element(element).perform()
        self.scroll_element(element)
        link = ElementsHelper(element).filter_tag('a')
        time.sleep(0.5)
        link[0].click()

    def click_el(self, element):

        """
                        Clicks on the element. Accepts an element containing an <a> tag.
                        Mouse hover is simulated
                        :param element: page element that contains the desired link
                        """
        
        self.actions.move_to_element(element).perform()
        self.scroll_element(element)
        time.sleep(0.8)
        element.click()








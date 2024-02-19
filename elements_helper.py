from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from search_base import SeacrhBase


class ElementsHelper:

    def __init__(self, elements):
        """
                Instrument for search
                :param elements: Elements finds webdriver.
                """

        if isinstance(elements, list):
            self.elements = elements
        else:
            self.elements = [elements]


    def find_by_tag(self, element: WebElement, tag: str) -> list:
        """
                Finds elements with specific html tags
                :param element: Webelement webdriver.
                :param tag: string name html tag, example 'div'
                """
        a = element.find_elements(By.TAG_NAME, tag)
        return a


    def find_by_text(self, list_web_el: list, text: str) -> WebElement:
        """
                Finds elements matching specific text
                :param list_web_el: list Webelements webdriver.
                :param text: string of text required for searching
                """
        for el in list_web_el:
            if el.text.lower() == text.lower():
                return el

    def _find_by_class(self, list_web_el: list, class_name: str) -> list:
        """
                        Finds elements containing a specific css class
                        :param list_web_el: list Webelements webdriver.
                        :param class_name: string of name css class
                        """
        elements_filter = []
        for el in list_web_el:
            if class_name.lower() in el.get_attribute("class").lower():
                elements_filter.append(el)
        self.elements = elements_filter
        return elements_filter

    def find_by_class(self, class_name: str) -> list:
        """
            Finds elements containing a specific css class
            (Can be run when creating an object)
            :param class_name: string of name css class
                                """
        return self._find_by_class(self.elements, class_name)

    def _filter_tag(self, list_web_el, tag):
        elements_filter = []
        for el in list_web_el:
            a = el.find_elements(By.TAG_NAME, tag)
            for i in a:
                elements_filter.append(i)
        return elements_filter

    def filter_tag(self, tag):
        return self._filter_tag(self.elements, tag)

    def find_class_in_tag(self, class_name, tag, text):
        self.elements = self._filter_tag(self.elements, tag)
        self.elements = self._find_by_class(self.elements, class_name)
        self.elements = self.find_by_text(self.elements, text)
        return self.elements


    def find_text_in_tag(self, text, tag):
        self.elements=self._filter_tag(self.elements, tag)
        self.elements=self.find_by_text(self.elements, text)
        return self.elements

    def find_link_for_text(self, text):
        a = self.find_text_in_tag(text, 'a')
        return a.get_attribute("href")


    def find_el_for_tag_and_text(self, text, tag):
        elelement = None
        for el in self.elements:
            a = self.find_by_tag(el,tag)
            for i in a:

                if i.text.lower() == text.lower():
                    elelement=el
        return elelement


    def get_size_img(self, element):
        # Получить ширину элемента
        width = element.size['width']
        # Получить высоту элемента
        height = element.size['height']
        return width, height

    def check_size_img(self):
        li = self._filter_tag(self.elements, 'img')
        li_s = []

        for i in li:
            li_s.append(self.get_size_img(i))


        if all(x == li_s[0] for x in li_s):
            return True



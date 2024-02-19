import time
import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from transliterate import translit

from config import *
from elements_helper import ElementsHelper
from other_methods import check_str_in
from search_base import SeacrhBase
from test_base import TestBase



class Test2(TestBase):

    def check_region(self,region, span_elements):
        a = span_elements.text

        name_region = a.split(' ')[0].lower()
        title_driver = self.driver.title.lower()
        url = self.driver.current_url
        city = self.find_element(id='city-id-2')[0].text

        region_lat = translit(region, 'ru', reversed=True)


        res_1 = check_str_in(url.split('/')[-1], region_lat, 4)
        res_2 = check_str_in(name_region, title_driver, 4)
        res_3 = check_str_in(name_region, city, 3)
        if res_1 and res_2 and res_3:
            return True
        else:
            return False

    def change_tegion(self, region):
        # Находим кнопку для того чтобы открть меню с выбором региона и кликаем по нему
        elements = self.find_element(class_name='sbis_ru-Region-Chooser__text')

        self.click_el(elements[1])

        elements = self.find_element(class_name='sbis_ru-Region-Panel__item')

        for i in elements:
            if check_str_in(i.text.lower(), region.lower(), len(region)):
                self.click_el(i)
                break


    def chapter_1(self):
        self.go_to_contacts()
        elements = self.find_element(class_name='s-Grid-col')
        find_el = ElementsHelper(elements).filter_tag('span')[0]
        #Проверяем текущий регион
        cheked_region = self.check_region('нижегородская', find_el)

        assert cheked_region==True, message_no_region_found
        print('Текущий регион соответсвует Нижегородской области')
        #меняем регион на камчатский
        self.change_tegion('камчатский')
        print('Изменил регион')
        #проверяем что регион изменился
        cheked_region_2 = self.check_region('камчатский', find_el)
        assert cheked_region==True, message_no_region_found
        print('Текущий регион соответсвует Камчатскому краю')





    def test_2(self):

        self.chapter_1()


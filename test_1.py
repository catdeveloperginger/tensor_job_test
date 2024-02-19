import time
import random

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from config import *
from elements_helper import ElementsHelper
from search_base import SeacrhBase
from test_base import TestBase



class Test1(TestBase):

    def chapter_1(self):
        self.go_to_contacts()
        """находим логотип и переходим по ссылке которая содрежится в нём так-как клик почему-то не работает
        сайт перехватывает клик по этому элементу, если работаешь черезе селениум
        """

        element = self.find_element(class_name='sbisru-Contacts__logo-tensor')

        cl = self.click_img_link('Разработчик системы СБИС — компания «Тензор»', element)
        assert cl==True, message_no_element_found

        #


    def chapter_2(self):
        """Очень странно почему-то при клике на банер selenium перекидывает на страницу которая содержит в ссылке dev и
        он не находит нужные элементы, всеравно приходится вручную прописывать переход по ссылке
        """

        self.switch_tab('тензор')


        #Ищем блок который содержит текст Сила в людях
        elements = self.find_element(class_name='tensor_ru-Index__block4-content')
        find_el = ElementsHelper(elements).find_text_in_tag('сила в людях','p')

        assert find_el, message_no_element_found
        print('Элемент с текстом "Сила в людях" найден')
        self.scroll_element(find_el)
        time.sleep(3)
        find_el_2 = ElementsHelper(elements).find_class_in_tag(class_name='tensor_ru-Index__card-text', tag='p', text='подробнее')
        assert find_el_2, message_no_element_found
        print('Элемент с текстом "Подробнее" найден')
        self.click_link(find_el_2)



    def chapter_3(self):

        # Проверяем текущую ссылку, она должна быть
        check_link = self.check_current_url('https://tensor.ru/about')
        assert check_link, message_no_link_found
        print('Ссылка соотвествует https://tensor.ru/about')

        elements = self.find_element(class_name='tensor_ru-About__block3')
        #Находим элемент с заголовком h2 Работаем
        find_el = ElementsHelper(elements).find_el_for_tag_and_text('работаем', 'h2')

        assert find_el, message_no_element_found

        actions.move_to_element(find_el).perform()
        #Проверяем размеры изображений
        check_img = ElementsHelper(find_el).check_size_img()

        assert check_img, message_no_size_found
        print('Размеры всех изображений одинаковые')







    def test_1(self):
        #Переходим на сайт и ищем раздел с контактами и ищем банер и кликаем по нему
        self.chapter_1()

        time.sleep(random.randint(1, 5))

        #Ищем блок "Сила в людях" и кликаем на подробнее
        # self.chapter_2()

        # self.chapter_3()
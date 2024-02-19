import pytest
import time

from selenium import webdriver

from fake_useragent import UserAgent
from selenium.webdriver import ActionChains

from search_base import SeacrhBase



@pytest.fixture
def get_driver(request):
    options = webdriver.ChromeOptions()
    # ua = UserAgent(browsers=['edge', 'chrome'])
    agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'
    options.add_argument(f"user-agent={agent}")


    driver = webdriver.Chrome(options=options)
    actions = ActionChains(driver)
    request.cls.driver = driver
    request.cls.actions = actions
    yield driver
    time.sleep(5)
    driver.quit()


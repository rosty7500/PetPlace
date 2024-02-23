import time
import urllib.request

import selenium
from selenium.webdriver.common.by import By
from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.common.exceptions import NoSuchElementException
from pages.Category_Navigation import Category_Navigation


class Test_Category_navigation(BaseClass):
    def test_cat_nav(self):
        Category_navigation = Category_Navigation(self.driver)
        HomePage.pethealth_menu(self)
        time.sleep(2)
        Category_navigation.click_next_arrow_pagination()
        Category_navigation.append_page_no_url()







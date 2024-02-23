from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.HomePage import HomePage


class Category_Navigation:
    def __init__(self, driver):
        self.driver = driver

    pagination_next_arrow = (By.XPATH, "//span[@class='icon icon-chevron-wide']//*[name()='svg']")

    def click_next_arrow_pagination(self):
        try:
            self.pethealth = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='icon icon-chevron-wide']//*[name()='svg']"))).click()
        except StaleElementReferenceException:
            pass

    def append_page_no_url(self):
        f_url = self.driver.current_url
        l_number = [5, 20, 40, 50]
        url = f_url[:f_url.rfind('2')]
        for page_num in l_number:
            c_url = url + str(page_num)
            print(c_url)
            self.driver.get(c_url)








from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    ClickLogo = (By.XPATH, " //a[@aria-label='Navigate to homepage']//span[@class='icon icon-logo']//*[name()='svg']")
    petcare_menu_link = (By.XPATH, "//a[@id='menu']")
    pethealth_menu_link = (By.CSS_SELECTOR,"div[class='nav-sections'] li:nth-child(2) a:nth-child(1)")
    pet_bh_menu_link = (By.CSS_SELECTOR, "div[class='nav-sections'] li:nth-child(3) a:nth-child(1)")
    breedguide_menu_link = (By.CSS_SELECTOR, "div[class='nav-sections'] li:nth-child(4) a:nth-child(1)")
    petinsurance_menu_link = (By.CSS_SELECTOR, "div[class='nav-sections'] li:nth-child(5) a:nth-child(1)")
    learnaboutpetinsurance_menu_link = (By.CSS_SELECTOR, "div[class='nav-sections'] li:nth-child(6) a:nth-child(1)")


    def petcare_menu(self):
        return self.driver.find_element(*HomePage.petcare_menu_link).click()

    def petbandt_menu(self):
        return self.driver.find_element(*HomePage.pet_bh_menu_link).click()

    def breedguide_menu(self):
        return self.driver.find_element(*HomePage.breedguide_menu_link).click()


    def petinsurance_menu(self):
        return self.driver.find_element(*HomePage.petinsurance_menu_link).click()


    def learnaboutpet_menu(self):
        return self.driver.find_element(*HomePage.learnaboutpetinsurance_menu_link).click()


    @property
    def menutitle(self):
        return self.driver.title

    def pethealth_menu(self):
        self.pethealth = WebDriverWait(self.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='nav-sections'] li:nth-child(2) a:nth-child(1)"))).click()


    def clickLogo(self):
        return self.driver.find_element(*HomePage.ClickLogo)

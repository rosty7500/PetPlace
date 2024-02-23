from selenium.webdriver.common.by import By
from pages.HomePage import HomePage
from utilities.BaseClass import BaseClass
from selenium.common.exceptions import NoSuchElementException



class Test_MenuLinks(BaseClass):

    def test_menuLinks(self):

        try:
            homepage = HomePage(self.driver)
            homepage.petcare_menu()
            assert "Pet Care | PetPlace.com" == homepage.menutitle
            homepage.pethealth_menu()
            assert "Pet Wellness" in homepage.menutitle
            homepage.petbandt_menu()
            assert "Pet Behavior" in homepage.menutitle
            homepage.breedguide_menu()
            assert "Breed Guide" in homepage.menutitle
            homepage.petinsurance_menu()
            assert "Insurance" in homepage.menutitle
            homepage.learnaboutpet_menu()
            assert "Find the Right" == homepage.menutitle
            homepage.clickLogo()
        except AssertionError:
            print("Assert error")



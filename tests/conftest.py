import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")
def setup(request):
    service_ojb = Service()
    driver = webdriver.Chrome(service=service_ojb)
    #driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
    driver.get("https://www.petplace.com/")
    print(driver.title)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
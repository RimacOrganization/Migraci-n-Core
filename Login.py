from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class Login():
    def sap(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://fours.softtek.cloud:8400/fiori")

        element_user = driver.find_element(By.CSS_SELECTOR, '#USERNAME_FIELD-inner')
        element_user.click()
        element_user.send_keys("DCHR1")

        element_pwd = driver.find_element(By.CSS_SELECTOR, '#PASSWORD_FIELD-inner')
        element_pwd.click()
        element_pwd.send_keys("Softtek*123rpa")
        self.test_loading(driver)
        time.sleep(30)

    def test_loading(driver):
        try:
            flag = True
            while flag:          
                element = driver.find_element(By.ID, 'th_freezeShield')
                loading = element.get_attribute("style")
                print(loading)
        except Exception as e:
            print(e)   

login = Login()
login.sap()
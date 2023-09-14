from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Solicitude():

    def find(self):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get("https://www.google.com")

        element = driver.find_element(By.CSS_SELECTOR, '#input')
        element.click()
        element.send_keys("Automation witch ipa")

login = Solicitude()
login.find()
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Core.Espera import Espera

class Base:
    
    def __init__(self, driver):
        self.driver = driver

    def sendkeys(self, locator, text):
          WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def click(self, locator):
          WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click()
        
    def select_dropdown(self, locator, text):
        select =  WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator))
        select.select_by_visible_text(text)

    def select_dynamic_dropdown(self, locator, text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).click()
        inputField = self.driver.find_element(By.XPATH,"//kendo-popup/div/span/input")
        inputField.send_keys(text)
        firstOption = self.driver.find_element(By.XPATH,"//kendo-list/div/ul/li[1]")
        firstOption.click()
        
    def read_text(self, locator):
        text = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(locator)).text
        return text
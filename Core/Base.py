from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

class Base:
    
    def __init__(self, driver):
        self.driver = driver

    def sendkeys(self, locator, text):
          WebDriverWait(self.driver,40).until(EC.visibility_of_element_located(locator),f"timeout has been exceeded then element could not be found, thus keys were not sent on this element: {locator}").send_keys(text)

    def click(self, locator):
        try:
          WebDriverWait(self.driver,40).until(EC.visibility_of_element_located(locator),f"timeout has been exceeded then this element {locator} could not be found, thus it could not be clicked").click()
        except(ElementClickInterceptedException):
            print("Exception")

        
    def select_dropdown(self, locator, text):
        select =  WebDriverWait(self.driver,40).until(EC.visibility_of_element_located(locator),f"timeout has been exceeded then this element {locator} could not be found, thus it could not be selected")
        select.select_by_visible_text(text)

    def select_dynamic_dropdown(self, locator, text):
        WebDriverWait(self.driver,40).until(EC.visibility_of_element_located(locator),f"timeout has been exceeded then this element {locator} could not be found, thus it could not select a item from the dropdown").click()
        inputField = self.driver.find_element(By.XPATH,"//kendo-popup/div/span/input")
        inputField.send_keys(text)
        firstOption = self.driver.find_element(By.XPATH,"//kendo-list/div/ul/li[1]")
        firstOption.click()
        
    def read_text(self, locator):
        text = WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(locator),f"timeout has been exceeded then element {locator} could not be found, thus it could not be read").text
        return text

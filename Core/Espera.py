from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep

class Espera:
    @staticmethod
    def wait_for_element_to_be_located(driver, locator):
        try:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located(locator),f"timeout has been exceeded then this {locator} could not be located")
        except TimeoutException:
            print("Timed out waiting for element to appear")

    @staticmethod
    def wait_for_url_to_contain(driver, url):
            try:
                WebDriverWait(driver, 30).until(EC.url_contains(url),f"timeout has been exceeded then url was different from {url}")
            except TimeoutException:
                print("Timed out waiting for url to be")

    @staticmethod
    def wait_for_element_to_dissapear(driver, locator):
        try:
            WebDriverWait(driver, 30).until(EC.invisibility_of_element(locator),f"timeout has been exceeded then this {locator} was still on screen")
        except TimeoutException:
            print("Timed out waiting for element to disappear")

    @staticmethod
    def wait_mask_loading_drpdown(driver):
        loadingMask = (By.XPATH,"//span[@class='k-icon k-i-loading']")
        Espera.wait_for_element_to_dissapear(driver, loadingMask)

    @staticmethod
    def wait_mask_loading(driver):
        loadingMask = (By.ID,"loading-bar-spinner")
        Espera.wait_for_element_to_dissapear(driver, loadingMask)


    @staticmethod
    def wait_seconds(seconds):
        sleep(seconds)

 
            

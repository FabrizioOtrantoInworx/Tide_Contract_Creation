from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from time import sleep

class Espera:
    @staticmethod
    def wait_for_element_to_be_located(driver, locator):
        try:
            WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("Timed out waiting for element to appear")

    @staticmethod
    def wait_for_Url_To_Contain(driver, url):
            try:
                WebDriverWait(driver, 5).until(EC.url_contains(url))
            except TimeoutException:
                print("Timed out waiting for url to be")

    @staticmethod
    def wait_for_element_to_dissapear(driver, locator):
        try:
            WebDriverWait(driver, 5).until(EC.invisibility_of_element(locator))
        except TimeoutException:
            print("Timed out waiting for element to disappear")

    @staticmethod
    def wait_mask_loading(driver):
        loadingMask = (By.ID,"loading-bar-spinner")
        Espera.wait_for_element_to_dissapear(driver, loadingMask)

    @staticmethod
    def wait_seconds(seconds):
        sleep(seconds)
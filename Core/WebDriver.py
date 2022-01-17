from selenium import webdriver
from Core.Configuration import Configuration

class WebDriver:

    @staticmethod
    def start_driver():
        browser = Configuration.set_browser()
        url = Configuration.set_url()
        rutaDriver = Configuration.set_ruta_driver()

        if(browser == "chrome"):
            driver = webdriver.Chrome(executable_path= rutaDriver + "chromedriver.exe")
        elif(browser == "firefox"):
            driver = webdriver.Firefox(executable_path= rutaDriver + "geckodriver.exe")
        elif(browser == "edge"):
            driver= webdriver.Edge(executable_path=rutaDriver + "msedgedriver.exe")
        else:
            driver = webdriver.Chrome(executable_path=rutaDriver)


        driver.maximize_window()
        driver.get (url)
        
        return driver




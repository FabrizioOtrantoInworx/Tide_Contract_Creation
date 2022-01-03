from selenium import webdriver
from Core.Configuration import Configuration

class WebDriver:

    @staticmethod
    def Start_Driver():
        browser = Configuration.setBrowser()
        url = Configuration.setUrl()
        rutaDriver = Configuration.setRutaDriver()

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




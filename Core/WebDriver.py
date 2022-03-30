from selenium import webdriver
from Core.Configuration import Configuration
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

class WebDriver:

    @staticmethod
    def start_driver():
        browser = Configuration.set_browser()
        url = Configuration.set_url()
        rutaDriver = Configuration.set_ruta_driver()

        if(browser == "chrome"):
            driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        elif(browser == "firefox"):
            driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif(browser == "edge"):
            driver= webdriver.Edge(EdgeChromiumDriverManager().install())
        else:
            driver = webdriver.Chrome(executable_path=rutaDriver)


        driver.maximize_window()
        driver.get(url)
        
        return driver




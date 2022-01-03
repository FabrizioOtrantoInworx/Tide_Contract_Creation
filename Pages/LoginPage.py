from selenium.webdriver.common.by import By
from Core.Base import Base
from Core.Configuration import Configuration
from Core.Espera import Espera

class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_Url_To_Contain(driver,"microsoftonline")

    def WriteEmail(self, email):
        emailField = (By.ID,"i0116")
        self.sendkeys(emailField, email)

    def ClickNext(self):
        nextBtn = (By.ID,"idSIButton9")
        Espera.wait_seconds(2)
        self.click(nextBtn)
    
    def WritePassword(self, password):
        passwordField = (By.ID, "i0118")
        self.sendkeys(passwordField, password)

    def Login(self):
        username = Configuration.setUsername()
        self.WriteEmail(username) 
        self.ClickNext()
        password = Configuration.setPassword()
        self.WritePassword(password)
        self.ClickNext()
        self.ClickNext()


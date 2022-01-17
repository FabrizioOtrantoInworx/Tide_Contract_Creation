from selenium.webdriver.common.by import By
from Core.Base import Base
from Core.Configuration import Configuration
from Core.Espera import Espera

class LoginPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_url_to_contain(driver,"microsoftonline")

    def write_email(self, email):
        emailField = (By.ID,"i0116")
        self.sendkeys(emailField, email)

    def click_next(self):
        nextBtn = (By.ID,"idSIButton9")
        Espera.wait_seconds(2)
        self.click(nextBtn)
    
    def write_password(self, password):
        passwordField = (By.ID, "i0118")
        self.sendkeys(passwordField, password)

    def login(self):
        username = Configuration.set_username()
        self.write_email(username) 
        self.click_next()
        password = Configuration.set_password()
        self.write_password(password)
        self.click_next()
        self.click_next()



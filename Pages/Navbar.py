from selenium.webdriver.common.by import By
from Core.Base import Base
from Core.Espera import Espera

class NavBar(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_contract_link(self):
        Espera.wait_mask_loading(self.driver)
        contractLink = (By.ID,"a_Topnav_Contracts")
        self.click(contractLink)

    def click_tide_logo(self):
        tideLogoBtn = (By.ID,"TideLogo")
        self.click(tideLogoBtn)
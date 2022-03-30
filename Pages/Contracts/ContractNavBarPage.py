from selenium.webdriver.common.by import By
from Core.Base import Base
from Core.Espera import Espera

class ContractNavBarPage(Base):

    def __init__(self, driver):
        super().__init__(driver)

    def click_details_tab(self):
        details_tab = (By.ID,"a_contract_details")
        self.click(details_tab)

    def click_add_section_tab(self):
        add_section_tab = (By.ID,"a_contract_addSection")
        self.click(add_section_tab)

    def click_reporting_channels_tab(self):
        reporting_channels_tab = (By.ID,"a_contract_reportingchannels")
        self.click(reporting_channels_tab)


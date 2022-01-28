from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera

class ContractPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_url_to_contain(self.driver,"contractlist")
        Espera.wait_mask_loading(self.driver)
        


    def click_contract_api_log_btn(self):
        contractApiLogBtn = (By.ID,"btn_contractList_contractApiLog")
        self.click(contractApiLogBtn)

    def click_add_contract_btn(self):
        addContractBtn = (By.ID,"btn_contractList_addContract")
        self.click(addContractBtn)


    

        
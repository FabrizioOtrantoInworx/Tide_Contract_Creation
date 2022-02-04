from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera

class ContractDetailPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_url_to_contain(self.driver, "main")
        Espera.wait_mask_loading(self.driver)

    def click_coverholder_tab(self):
        coverholder_tab = (By.ID,"a_details_coverholder")
        self.click(coverholder_tab)

    def click_contract_status_btn(self):
        contract_status_btn = (By.ID,"btn_contractStatus")
        self.click(contract_status_btn)
        Espera.wait_mask_loading(self.driver)
        #Espera.wait_seconds(2)


    def select_contract_status(self, text):
        contrat_status_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_contractStatus']/span/span[2]")
        self.select_dynamic_dropdown(contrat_status_select, text)

        
    def click_save_btn(self):
        save_btn = (By.ID,"btn_contractStatusUpdate_save")
        self.click(save_btn)

    

    
 
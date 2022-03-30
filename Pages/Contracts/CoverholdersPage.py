from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera

class CoverholderPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_url_to_contain(self.driver, "coverholder")
        Espera.wait_mask_loading(self.driver)



    
    def click_add_coverholder(self):
        add_coverholder_btn = (By.ID,"btn_coverholders_addCoverholder")
        self.click(add_coverholder_btn)

        
        
    def select_coverholder(self, text):
        coverholder_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_coverholderId']/span/span[2]")
        Espera.wait_mask_loading_drpdown(self.driver)

        self.select_dynamic_dropdown(coverholder_select, text)
        
        
    def click_save_btn(self):
        save_btn = (By.ID,"btn_addEditCoverholders_save")
        self.click(save_btn)
        Espera.wait_mask_loading(self.driver)
        Espera.wait_mask_loading(self.driver)

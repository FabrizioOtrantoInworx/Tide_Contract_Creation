from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera

class AddContractPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_url_to_contain(self.driver, "create")
        Espera.wait_mask_loading(self.driver)

    def write_umr(self, text):
        Espera.wait_mask_loading(self.driver)
        umrField = (By.ID,"txt_umr")
        self.sendkeys(umrField, text)

    def select_currency(self,text):     
        currencySelect = (By.XPATH,"//kendo-dropdownlist[@id='ddl_contractCurrency']/span/span[2]")
        self.select_dynamic_dropdown(currencySelect, text)

    def click_add_folder_btn(self):
        addFolderBtn = (By.ID,"btn_createContract_addFolder")
        self.click(addFolderBtn)

    def select_folder_type(self,text):
        folderTypeSelect = (By.XPATH,"//kendo-dropdownlist[@id='ddl_folderTypeId']/span/span[2]")
        self.select_dynamic_dropdown(folderTypeSelect,text)

    def select_division(self,text):
        folderTypeSelect = (By.XPATH,"//kendo-dropdownlist[@id='ddl_divisionId']/span/span[2]")
        self.select_dynamic_dropdown(folderTypeSelect,text)
    
    def click_save_btn(self):
        saveBtn = (By.ID,"btn_folderAdd_ok")
        self.click(saveBtn)
        Espera.wait_mask_loading(self.driver)

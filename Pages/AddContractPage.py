from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera

class AddContractPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_Url_To_Contain(self.driver, "create")
        Espera.wait_mask_loading(self.driver)

    def WriteUmr(self, text):
        Espera.wait_mask_loading(self.driver)
        umrField = (By.ID,"txt_umr")
        self.sendkeys(umrField, text)

    def SelectCurrency(self,text):     
        currencySelect = (By.XPATH,"//kendo-dropdownlist[@id='ddl_contractCurrency']/span/span[2]")
        self.SelectDynamicDropdown(currencySelect, text)

    def ClickAddFolderBtn(self):
        addFolderBtn = (By.ID,"btn_createContract_addFolder")
        self.click(addFolderBtn)

    def SelectFoldertype(self,text):
        folderTypeSelect = (By.XPATH,"//kendo-dropdownlist[@id='ddl_folderTypeId']/span/span[2]")
        self.SelectDynamicDropdown(folderTypeSelect,text)

    def SelectDivision(self,text):
        folderTypeSelect = (By.XPATH,"//kendo-dropdownlist[@id='ddl_divisionId']/span/span[2]")
        self.SelectDynamicDropdown(folderTypeSelect,text)
    
    def ClickSaveBtn(self):
        saveBtn = (By.ID,"btn_folderAdd_ok")
        self.click(saveBtn)
        Espera.wait_mask_loading(self.driver)

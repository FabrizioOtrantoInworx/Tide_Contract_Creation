from selenium.webdriver.common.by import By
from Core.Espera import Espera
from Core.Base import Base
import json

class ContratApiLogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_Url_To_Contain(self.driver, "contractsapilog")
        Espera.wait_mask_loading(self.driver)


    def ClickUMRFilterBtn(self,):
        umrFilterBtn = (By.ID,"filterIcnuniqueMarketReference")
        Espera.wait_for_element_to_be_located(self.driver, umrFilterBtn )
        self.click(umrFilterBtn)

    def ClickSSRFilterBtn(self,):
        ssrFilterBtn = (By.ID,"filterIcnsourceSystemReference")
        Espera.wait_for_element_to_be_located(self.driver, ssrFilterBtn )
        self.click(ssrFilterBtn)

    def writeinSearchField(self, umr):
        searchField = (By.ID,"lbl_search")
        self.sendkeys(searchField, umr)
        
    def ClickCheckBtn(self, umr):
        checkbtnID = "chk_" + umr + "_0"
        checkBtn = (By.ID, checkbtnID)
        self.click(checkBtn)

    def ClickFilterBtn(self):
        FilterButton = (By.XPATH,"//button[contains(text(),'Filter')]")
        self.click(FilterButton)

    def ClickReviewErrorsBtn(self):
        Espera.wait_mask_loading(self.driver)
        reviewErrorsBtn = (By.XPATH,"//button[contains(text(),'REVIEW ERRORS')]")
        self.click(reviewErrorsBtn)

    def ClickOkBtn(self):
        okBtn = (By.ID,"btn_ok")
        self.click(okBtn)

    def readErrors(self, errorNumber):
        Espera.wait_mask_loading(self.driver)
        errors = self.driver.find_elements(By.XPATH,"//span[@class='error-note-desc-red toolTip-text ng-star-inserted']")
        return errors[errorNumber].text
        
        
    def readStatus(self):
        Espera.wait_mask_loading(self.driver)
        statusSpan = (By.XPATH,"//*[@id='span_errorStatus_0']/span")
        return self.readText(statusSpan)
         

       
    def wait_until_contract_is_Load_into_tide(self, umr):
        self.ClickUMRFilterBtn()
        self.writeinSearchField(umr)
        Espera.wait_seconds(6)
        self.noDataFoundElement = self.driver.find_element(By.XPATH,"//multicheck-filter[@id='mdl_uniqueMarketReference']/div[2]").text
        print(self.noDataFoundElement)
        self.contador = 0
        while self.noDataFoundElement == "No Data Found":
            self.driver.refresh()
            Espera.wait_mask_loading(self.driver)
            self.ClickUMRFilterBtn()
            self.writeinSearchField(umr)
            Espera.wait_seconds(6)
            self.noDataFoundElement = self.driver.find_element(By.XPATH,"//multicheck-filter[@id='mdl_uniqueMarketReference']/div[2]").text
            self.contador = self.contador + 1
            if self.noDataFoundElement == "0 items selected" or self.contador == 60:
                break
            





        
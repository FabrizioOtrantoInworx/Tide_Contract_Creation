from tkinter.constants import E
from selenium.webdriver.common.by import By
from Core.Espera import Espera
from Core.Base import Base
import json

class ContratApiLogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_url_to_contain(self.driver, "contractsapilog")
        Espera.wait_mask_loading(self.driver)


    def click_umr_filter_btn(self,):
        umrFilterBtn = (By.ID,"filterIcnuniqueMarketReference")
        Espera.wait_for_element_to_be_located(self.driver, umrFilterBtn )
        self.click(umrFilterBtn)

    def click_ssr_filter_btn(self,):
        ssrFilterBtn = (By.ID,"filterIcnsourceSystemReference")
        Espera.wait_for_element_to_be_located(self.driver, ssrFilterBtn )
        self.click(ssrFilterBtn)

    def writeinSearchField(self, umr):
        searchField = (By.ID,"lbl_search")
        self.sendkeys(searchField, umr)
        
    def click_check_btn(self, umr):
        checkbtnID = "chk_" + umr + "_0"
        checkBtn = (By.ID, checkbtnID)
        self.click(checkBtn)

    def click_filter_btn(self):
        FilterButton = (By.XPATH,"//button[contains(text(),'Filter')]")
        self.click(FilterButton)

    def click_review_errors_btn(self):
        Espera.wait_mask_loading(self.driver)
        reviewErrorsBtn = (By.XPATH,"//button[contains(text(),'REVIEW ERRORS')]")
        self.click(reviewErrorsBtn)

    def click_ok_btn(self):
        okBtn = (By.ID,"btn_ok")
        self.click(okBtn)

    def read_errors(self, errorNumber):
        Espera.wait_mask_loading(self.driver)
        errors = self.driver.find_elements(By.XPATH,"//span[@class='error-note-desc-red toolTip-text ng-star-inserted']")
        return errors[errorNumber].text
        
        
    def read_status(self):
        Espera.wait_mask_loading(self.driver)
        statusSpan = (By.XPATH,"//*[@id='span_errorStatus_0']/span")
        return self.read_text(statusSpan)
         

       
    def wait_until_contract_is_Loaded_into_tide_With_Umr(self, umr):
        self.click_umr_filter_btn()
        self.writeinSearchField(umr)
        Espera.wait_seconds(6)
        self.noDataFoundElement = self.driver.find_element(By.XPATH,"//multicheck-filter[@id='mdl_uniqueMarketReference']/div[2]").text
        print(self.noDataFoundElement)
        self.contador = 0
        while self.noDataFoundElement == "No Data Found":
            self.driver.refresh()
            Espera.wait_mask_loading(self.driver)
            self.click_umr_filter_btn()
            self.writeinSearchField(umr)
            Espera.wait_seconds(6)
            self.noDataFoundElement = self.driver.find_element(By.XPATH,"//multicheck-filter[@id='mdl_uniqueMarketReference']/div[2]").text
            self.contador = self.contador + 1
            if self.noDataFoundElement == "0 items selected" or self.contador == 80:
                Espera.wait_mask_loading(self.driver)
                Espera.wait_seconds(2)
                break

    def wait_until_contract_is_Loaded_into_tide_With_Lcr(self, lcr):
        self.click_ssr_filter_btn()
        self.writeinSearchField(lcr)
        Espera.wait_seconds(6)
        self.noDataFoundElement = self.driver.find_element(By.XPATH,"//multicheck-filter[@id='mdl_sourceSystemReference']/div[2]").text
        print(self.noDataFoundElement)
        self.contador = 0
        while self.noDataFoundElement == "No Data Found":
            self.driver.refresh()
            Espera.wait_mask_loading(self.driver)
            self.click_ssr_filter_btn()
            self.writeinSearchField(lcr)
            Espera.wait_seconds(6)
            self.noDataFoundElement = self.driver.find_element(By.XPATH,"//multicheck-filter[@id='mdl_sourceSystemReference']/div[2]").text
            self.contador = self.contador + 1
            if self.noDataFoundElement == "0 items selected" or self.contador == 80:
                Espera.wait_mask_loading(self.driver)
                Espera.wait_seconds(2)
                break
            





        
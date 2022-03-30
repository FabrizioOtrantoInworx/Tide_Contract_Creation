from tkinter.constants import E
from selenium.webdriver.common.by import By
from Core.Espera import Espera
from Core.Base import Base
from Core.Utilidades.Utilidades import Utilidades
from Pages.Contracts.Enumerations.Identifiers import Identifiers


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
         

       
    def wait_until_contract_is_Loaded_into_tide(self, id, search_by = Identifiers.UMR):
        if search_by == Identifiers.UMR:
            self.click_umr_filter_btn()
        elif search_by == Identifiers.LCR:
            self.click_ssr_filter_btn()       
        self.writeinSearchField(id)
        self.noDataFoundLocator = (By.XPATH,"//div[contains(text(),'No Data Found')]")
        self.contador = 0
        utilidades = Utilidades(self.driver)
        while utilidades.check_if_element_exist(self.noDataFoundLocator) == True:
            self.driver.refresh()
            Espera.wait_mask_loading(self.driver)
            Espera.wait_seconds(5)
            if search_by == Identifiers.UMR:
                self.click_umr_filter_btn()
            elif search_by == Identifiers.LCR:
                self.click_ssr_filter_btn()       
            self.writeinSearchField(id)
            self.noDataFoundLocator = (By.XPATH,"//div[contains(text(),'No Data Found')]")
            self.contador = self.contador + 1
            if self.contador == 50 or utilidades.check_if_element_exist(self.noDataFoundLocator) == False:
                Espera.wait_mask_loading(self.driver)
                break



        
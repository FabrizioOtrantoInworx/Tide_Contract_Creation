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

    def writeUMR(self):
        searchField = (By.ID,"lbl_search")
        t= open ("C:/PythonAutomation/Scripts/Jsons/template.json")
        dataTemplate = json.load(t)
        UMR = dataTemplate["UMR"]
        self.sendkeys(searchField, UMR)
        
    def ClickCheckBtn(self):
        t= open ("C:/PythonAutomation/Scripts/Jsons/template.json")
        dataTemplate = json.load(t)
        UMR = dataTemplate["UMR"]
        checkbtnID = "chk_" + UMR + "_0"
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

    def assertErrors(self):
        Espera.wait_mask_loading(self.driver)
        errors = self.driver.find_elements(By.XPATH,"//span[@class='error-note-desc-red toolTip-text ng-star-inserted']")
        error = errors[0].text
        if(error == "[Broker] supplied cannot be matched to a valid Tide [Company/Division]."):
            print("pass")
        else:
            print("failed")




        
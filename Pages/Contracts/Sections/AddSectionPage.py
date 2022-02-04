from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera

class AddSectionPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_mask_loading(self.driver)

    
    def write_market_section_reference(self,text):
        market_section_reference_field = (By.ID,"txt_sectionMarketSectionReference")
        self.sendkeys(market_section_reference_field, text)

    def write_market_section_description(self,text):
        market_section_description_field = (By.ID,"txt_sectionMarketSectionDescription")
        self.sendkeys(market_section_description_field, text)

    def write_brokerage(self,text):
        brokerage_field = (By.ID,"txt_sectionBrokerage")
        self.sendkeys(brokerage_field, text)

    def write_coverholder_commission(self,text):
        coverholder_commission_field = (By.ID,"txt_sectionCoverholderComission")
        self.sendkeys(coverholder_commission_field, text)

    def write_additional_deductions(self,text):
        additional_deductions_field = (By.ID,"txt_ssectionAddtionalDeductions")
        self.sendkeys(additional_deductions_field, text)    
        
    def select_class_bussiness(self, text):
        class_bussiness_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_sectionClassOfBusiness']/span/span[2]")
        self.select_dynamic_dropdown(class_bussiness_select, text)


    def select_section_currency(self, text):
        section_currency_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_sectionSectionCurrency']/span/span[2]")
        self.select_dynamic_dropdown(section_currency_select, text)
        
    def write_section_maximum_limit_liability(self,text):
        section_maximum_limit_liability_field = (By.ID,"txt_sectionMaximumLimitLiability")
        self.sendkeys(section_maximum_limit_liability_field, text)

    def select_risk_ratting(self, text):
        risk_rating_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_sectionConductRiskRating']/span/span[2]")
        self.select_dynamic_dropdown(risk_rating_select, text)
        
    def click_save_btn(self):
        save_btn = (By.ID,"btn_sectionAdd")
        self.click(save_btn)
        Espera.wait_mask_loading(self.driver)
        Espera.wait_mask_loading(self.driver)

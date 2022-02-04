from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera

class InsurerPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_mask_loading(self.driver)

    def click_insurer_tab(self):
        insurer_tab = (By.ID,"a_contractSections_market")
        self.click(insurer_tab)
        Espera.wait_mask_loading(self.driver)

    def click_add_insurer(self):
        add_insurer_btn = (By.ID,"btn_AddMarket")
        self.click(add_insurer_btn)
        Espera.wait_mask_loading(self.driver)



    def select_insurer(self, text):
        insurer_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_sectionMarketInsurer']/span/span[2]")
        self.select_dynamic_dropdown(insurer_select, text)


    def write_written_line(self,text):
        written_line_field = (By.ID,"txt_sectionMarketWrittenLinePercentage")
        self.sendkeys(written_line_field, text)

    def write_estimated_signed_line(self,text):
        estimated_signed_line_field = (By.ID,"txt_sectionMarketEstimatedSignedLinePercentage")
        self.sendkeys(estimated_signed_line_field, text)


    def click_add_insurer(self):
        add_insurer_btn = (By.ID,"btn_AddMarket")
        self.click(add_insurer_btn)

    def mark_coverholder_as_lead(self):
        coverholder_lead_yes_btn = (By.ID,"rbn_sectionMarketIsLead_true")
        self.click(coverholder_lead_yes_btn)

    def mark_coverholder_as_breach_administrator(self):
        coverholder_breach_administrator_yes_btn = (By.ID,"lbl_sectionMarketBreachAdministrator_true")
        self.click(coverholder_breach_administrator_yes_btn)

    def click_save_btn(self):
        save_btn = (By.ID,"btn_marketSave")
        self.click(save_btn)
        Espera.wait_mask_loading(self.driver)
        Espera.wait_mask_loading(self.driver)
        Espera.wait_seconds(2)


        

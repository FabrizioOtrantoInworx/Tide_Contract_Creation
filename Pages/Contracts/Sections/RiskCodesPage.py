from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera

class RiskCodesPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_mask_loading(self.driver)

    def click_risk_codes_tab(self):
        risk_codes_tab = (By.ID,"a_contractSections_riskCode")
        self.click(risk_codes_tab)
        Espera.wait_mask_loading(self.driver)


    def click_add_risk_code(self):
        add_risk_code_btn = (By.ID,"btn_OpenAddRiskCodePopUp")
        self.click(add_risk_code_btn)
        Espera.wait_mask_loading(self.driver)


    def select_risk_code(self, text):
        risk_code_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_riskCodeLlyodsRiskCode']/span/span[2]")
        self.select_dynamic_dropdown(risk_code_select, text)


    def write_split_porcentage(self,text):
        split_field = (By.ID,"txt_riskCodeSplitPercentage")
        self.sendkeys(split_field, text)

    def click_save_btn(self):
        save_btn = (By.ID,"btn_riskCodeSave")
        self.click(save_btn)
        Espera.wait_mask_loading(self.driver)
        Espera.wait_mask_loading(self.driver)
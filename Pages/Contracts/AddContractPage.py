from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class AddContractPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_for_url_to_contain(self.driver, "create")
        Espera.wait_mask_loading(self.driver)

    def click_add_folder_btn(self):
        add_folder_btn = (By.ID,"btn_createContract_addFolder")
        self.click(add_folder_btn)

    def select_folder_type(self,text):
        folder_type_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_folderTypeId']/span/span[2]")
        self.select_dynamic_dropdown(folder_type_select,text)

    def select_division(self,text):
        division_Select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_divisionId']/span/span[2]")
        self.select_dynamic_dropdown(division_Select,text)
    
    def click_save_folder_btn(self):
        save_btn = (By.ID,"btn_folderAdd_ok")
        self.click(save_btn)
        Espera.wait_mask_loading(self.driver)

    def write_umr(self, text):
        Espera.wait_mask_loading(self.driver)
        umr_field = (By.ID,"txt_umr")
        self.sendkeys(umr_field, text)

    def select_currency(self,text):     
        currency_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_contractCurrency']/span/span[2]")
        self.select_dynamic_dropdown(currency_select, text)

    def select_settlement_currency(self, text):
        currency_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_contractSettlementCurrency']/span/span[2]")
        self.select_dynamic_dropdown(currency_select, text)

    def select_broker(self, text):
        broker_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_broker']/span/span[2]")
        self.select_dynamic_dropdown(broker_select, text)

    def write_inception_date(self, text):
        inception_date_field = self.driver.find_element(By.XPATH,"//kendo-datepicker[@id='dtpicker_inceptionDate']/span/kendo-dateinput/span/input")
        action = ActionChains(self.driver)
        action.send_keys_to_element(inception_date_field,Keys.RETURN)
        action.send_keys_to_element(inception_date_field,Keys.RETURN)
        action.send_keys_to_element(inception_date_field,text)
        action.perform()

    def write_expiry_date(self, text):
        expiry_date_field = self.driver.find_element(By.XPATH,"//kendo-datepicker[@id='dtpicker_expiryDate']/span/kendo-dateinput/span/input")
        action = ActionChains(self.driver)
        action.send_keys_to_element(expiry_date_field,Keys.RETURN)
        action.send_keys_to_element(expiry_date_field,Keys.RETURN)
        action.send_keys_to_element(expiry_date_field,text)
        action.perform()

    def move_mouse(self):
        action = ActionChains(self.driver)
        action.move_by_offset(100,200)
        action.perform()


    def click_save_btn(self):
        save_btn = (By.ID,"btn_createContract_save")
        self.click(save_btn)
        Espera.wait_mask_loading(self.driver)


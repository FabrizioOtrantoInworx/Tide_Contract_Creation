from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from Core.Base import Base
from Core.Espera import Espera

class ReportingChannelsPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        Espera.wait_mask_loading(self.driver)

    def click_add_reporting_channel(self):
        add_reporting_channel_btn = (By.ID,"btn_reportingChannel_add")
        self.click(add_reporting_channel_btn)
        Espera.wait_mask_loading(self.driver)

    def select_type(self, text):
        type_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_bordereauxTypeId']/span/span[2]")
        self.select_dynamic_dropdown(type_select, text)

    def select_frequency(self, text):
        frequency_select = (By.XPATH,"//kendo-dropdownlist[@id='ddl_frequency']/span/span[2]")
        self.select_dynamic_dropdown(frequency_select, text)

    def click_save_btn(self):
        save_btn = (By.ID,"btn_addEditReportingChannel_save")
        self.click(save_btn)
        Espera.wait_mask_loading(self.driver)
        Espera.wait_mask_loading(self.driver)
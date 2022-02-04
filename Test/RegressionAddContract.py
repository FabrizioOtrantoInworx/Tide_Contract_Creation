from Core.Espera import Espera
from Pages.Contracts.Sections.InsurerPage import InsurerPage
from Pages.Shared.LoginPage import LoginPage
from Pages.Contracts.ContractPage import ContractPage
from Pages.Contracts.AddContractPage import AddContractPage
from Pages.Contracts.ContractDetailPage import ContractDetailPage
from Pages.Contracts.CoverholdersPage import CoverholderPage
from Pages.Contracts.Sections.AddSectionPage import AddSectionPage
from Pages.Contracts.Sections.InsurerPage import InsurerPage
from Pages.Contracts.Sections.RiskCodesPage import RiskCodesPage
from Pages.Contracts.ReportingChannelsPage import ReportingChannelsPage
from Pages.Contracts.ContractNavBarPage import ContractNavBarPage
from Pages.Shared.HomePage import HomePage
from Core.WebDriver import WebDriver
import json
import pytest
from allure_commons.types import AttachmentType
import allure

@pytest.fixture()
def setup(): 
    global driver
    driver = WebDriver.start_driver()
    loginPage = LoginPage(driver)
    loginPage.login()
    yield
    #driver.close()

@allure.title("Create new contract")
@allure.description_html("""<h4>This test is to verify that a contract has been create successfully</h4>""")
def test_regression_contract_api_log_version_update_date_equal_current_data_time(setup):
        try:
            t = open("./Data/Contracts/Contract_template.json")
            dataTemplate = json.load (t)
            homePage = HomePage(driver)
            homePage.Navbar.click_contract_link()

            contractPage = ContractPage(driver)
            contractPage.click_add_contract_btn()
            
            add_contract_page = AddContractPage(driver)
            Espera.wait_seconds(1)
            add_contract_page.move_mouse()
            add_contract_page.click_add_folder_btn()
            add_contract_page.select_folder_type(dataTemplate['contract']['folder_type'])
            add_contract_page.select_division(dataTemplate['contract']['division'])
            add_contract_page.click_save_folder_btn()
            add_contract_page.write_umr(dataTemplate['contract']['umr'])
            add_contract_page.select_currency(dataTemplate['contract']['currency'])
            add_contract_page.write_inception_date(dataTemplate['contract']['inception_date'])
            add_contract_page.write_expiry_date(dataTemplate['contract']['expiry_date'])
            add_contract_page.select_settlement_currency(dataTemplate['contract']['settlement_currency'])
            add_contract_page.select_broker(dataTemplate['contract']['broker'])
            add_contract_page.click_save_btn()

            contract_details_page = ContractDetailPage(driver)
            contract_details_page.click_coverholder_tab()

            coverholder_page = CoverholderPage(driver)
            coverholder_page.click_add_coverholder()
            coverholder_page.select_coverholder("Aon UK Limited Reinsurance - 111680VGU")
            coverholder_page.click_save_btn()

            contract_navbar_page = ContractNavBarPage(driver)
            contract_navbar_page.click_add_section_tab()

            add_section_page = AddSectionPage(driver)
            add_section_page.write_market_section_reference(dataTemplate['section']['section_reference'])
            add_section_page.write_market_section_description(dataTemplate['section']['section_description'])
            add_section_page.write_brokerage(dataTemplate['section']['brokerage'])
            add_section_page.write_coverholder_commission(dataTemplate['section']['coverholder_commission'])
            add_section_page.write_additional_deductions(dataTemplate['section']['additional_deduction'])
            add_section_page.select_risk_ratting(dataTemplate['section']['risk_ratting'])
            add_section_page.select_class_bussiness(dataTemplate['section']['class_bussiness'])
            add_section_page.select_section_currency(dataTemplate['section']['section_Ccurrency'])
            add_section_page.write_section_maximum_limit_liability(dataTemplate['section']['section_maximum_limit_liability'])
            add_section_page.click_save_btn()

            insurer_page = InsurerPage(driver)
            insurer_page.click_insurer_tab()
            insurer_page.click_add_insurer()
            insurer_page.select_insurer(dataTemplate['insurer']['insurer'])
            insurer_page.write_written_line(dataTemplate['insurer']['written_line'])
            insurer_page.write_estimated_signed_line(dataTemplate['insurer']['estimated_signed_line'])
            insurer_page.mark_coverholder_as_lead()
            insurer_page.mark_coverholder_as_breach_administrator()
            insurer_page.click_save_btn()

            risk_code_page = RiskCodesPage(driver)
            risk_code_page.click_risk_codes_tab()
            risk_code_page.click_add_risk_code()
            risk_code_page.select_risk_code(dataTemplate['risk_code']['risk_code'])
            risk_code_page.write_split_porcentage(dataTemplate['risk_code']['split_porcentage'])
            risk_code_page.click_save_btn()

            contract_navbar_page.click_reporting_channels_tab()
            reporting_channel_page = ReportingChannelsPage(driver)
            reporting_channel_page.click_add_reporting_channel()
            reporting_channel_page.select_type(dataTemplate['reporting_channel']['type'])
            reporting_channel_page.select_frequency(dataTemplate['reporting_channel']['frequency'])
            reporting_channel_page.click_save_btn()

            contract_navbar_page.click_details_tab()
            contract_details_page.click_contract_status_btn()
            contract_details_page.select_contract_status("Signed")
            contract_details_page.click_save_btn()
            t.close()
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(f"Test have failed. \n\n {ex}", False)
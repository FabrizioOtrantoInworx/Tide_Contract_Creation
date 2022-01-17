from Core.Espera import Espera
from Pages.LoginPage import LoginPage
from Pages.ContractPage import ContractPage
from Pages.HomePage import HomePage
from Pages.ContratApiLogPage import ContratApiLogPage
from Pages.AddContractPage import AddContractPage
from Core.WebDriver import WebDriver
import json
import pytest

@pytest.fixture()
def setup(): 
    global driver
    driver = WebDriver.start_driver()
    loginPage = LoginPage(driver)
    loginPage.login()
    yield
    driver.close()

def test_RegressionContratApiLogTestVersionUpdateDateEqualCurrentDataTime(setup):
        t = open('./Data/SendJson/Templates/VersionUpdateDateEqualCurrentDataTimeTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Umr(umr)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        assert contratApiLogPage.read_status() =="-"
        


def test_RegressionContratApiLogTestContractWihoutUMR(setup):
        t = open('./Data/SendJson/Templates/ContractWihoutUMRTemplate.json')
        dataTemplate = json.load (t)
        lcr = dataTemplate['LloydsContractRef']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Lcr(lcr)
        contratApiLogPage.click_check_btn(lcr)
        contratApiLogPage.click_filter_btn()
        contratApiLogPage.click_review_errors_btn()
        assert contratApiLogPage.read_errors(0) == f"E004: UMR missing from contract; CONTRACTUMRISEMPTY; Contract with LloydsContractRef {lcr} does not have a valid UMR"
        contratApiLogPage.click_ok_btn()
        

def test_RegressionContratApiLogTestContractWihoutLCR(setup):
        t = open('./Data/SendJson/Templates/ContractWihoutLCRTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Umr(umr)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        contratApiLogPage.click_review_errors_btn()
        assert contratApiLogPage.read_errors(0) == f"E003: LloydsContractRef missing from contract; CONTRACTLLOYDSCONTRACTREFISEMPTY; Contract with UMR {umr} does not have a valid Lloyds Contract Ref"
        contratApiLogPage.click_ok_btn()
        

def test_RegressionContratApiLogTestContractStatusNameAndContractTypeName(setup):
        t = open('./Data/SendJson/Templates/ContractStatusNameAndContractTypeNameTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Umr(umr)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        assert contratApiLogPage.read_status() =="-"
        


def test_RegressionContratApiLogTestContractTypeNameAndMigratedFlagMissing(setup):
        t = open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagMissingTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Umr(umr)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        assert contratApiLogPage.read_status() =="-"
        

def test_RegressionContratApiLogTestContractTypeNameAndMigratedFlagFalse(setup):
        t = open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagFalseTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Umr(umr)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        assert contratApiLogPage.read_status() =="-"
        


def test_RegressionContratApiLogTestContractWithoutContractCurrency(setup):
        t = open('./Data/SendJson/Templates/ContractWithoutContractCurrencyTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Umr(umr)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        contratApiLogPage.click_review_errors_btn()
        assert contratApiLogPage.read_errors(0) == "L003: Invalid DCOM Contract; Unable to load contract into TIDE."
        contratApiLogPage.click_ok_btn()
        

def test_RegressionContratApiLogTestContractStatusNameEqualRegistered(setup):

        t = open('./Data/SendJson/Templates/ContractStatusNameEqualRegisteredTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Umr(umr)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        assert contratApiLogPage.read_status() =="-"
        



def test_RegressionContratApiLogTestMigratedFlagTrueAndIsMigratedDraftTrue(setup):
        t = open('./Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Umr(umr)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        assert contratApiLogPage.read_status() =="-"
        

def test_RegressionContratApiLogTestContractWithSameUmrAndLcr(setup):
        t = open('./Data/SendJson/Templates/ContractWithSameUmrAndLcrTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide_With_Umr(umr)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        assert contratApiLogPage.read_status() =="-"
        



def RegressionAddContract():
    try:
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_add_contract_btn()

        addContractPage = AddContractPage(driver)
        addContractPage.click_add_folder_btn()
        addContractPage.select_folder_type("Binder")
        addContractPage.select_division("AT_Test Insurer 1 - Schedule Service")
        addContractPage.click_save_btn()
        addContractPage.write_umr("aaa")
        addContractPage.select_currency("ars")
        
    except Exception as ex:
        print(ex)
    

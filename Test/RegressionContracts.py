from Pages.Shared.LoginPage import LoginPage
from Pages.Contracts.ContractPage import ContractPage
from Pages.Shared.HomePage import HomePage
from Pages.Contracts.ContratApiLogPage import ContratApiLogPage
from Core.WebDriver import WebDriver
from Pages.Contracts.Enumerations.Identifiers import Identifiers
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
    driver.close()

@allure.title("Current Version Update Date")
@allure.description_html("""<h4>This test is to verify that contract does not have errors on tide</h4>""")
def test_regression_contract_api_log_version_update_date_equal_current_data_time(setup):
        try:
                happy_path('VersionUpdateDateEqualCurrentDataTimeTemplate.json')
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(f"Test have failed. \n\n {ex}", False)

@allure.title("Contract without umr")
@allure.description_html("""<h4>This test is to verify that contract have errors on tide</h4>""")
def test_regression_contrat_api_log_contract_wihout_umr(setup):
        try:
                error_text = "E004: UMR missing from contract; CONTRACTUMRISEMPTY"
                error_path('ContractWihoutUMRTemplate.json',error_text, Identifiers.LCR)
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)

@allure.title("Contract without lcr")
@allure.description_html("""<h4>This test is to verify that contract does not have errors on tide</h4>""")
def test_regression_contract_api_log_contract_wihout_lcr(setup):
        try:
                error_text = "E003: LloydsContractRef missing from contract; CONTRACTLLOYDSCONTRACTREFISEMPTY; Contract with UMR"
                error_path('ContractWihoutLCRTemplate.json', error_text, Identifiers.UMR)
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)

@allure.title("ContractStatusName equal to active & contractTypeName equal to Binding Authority Agreement")
@allure.description_html("""<h4>This test is to verify that contract does not have errors on tide</h4>""")
def test_regression_contract_api_log_Contract_status_Name_and_contract_type_name(setup):
        try:
                happy_path('ContractStatusNameAndContractTypeNameTemplate.json')
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)

@allure.title("ContractTypeName equal to Twin Contract & missing TestMigratedFlag")
@allure.description_html("""<h4>This test is to verify that contract does not have errors on tide</h4>""")
def test_regression_contract_api_log_contract_type_name_and_migrated_flag_missing(setup):
        try:
                happy_path('ContractTypeNameAndMigratedFlagMissingTemplate.json')
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)

@allure.title("ContractTypeName is equal to Service Company Agreement & migratedFlag is False")
@allure.description_html("""<h4>This test is to verify that contract does not have errors on tide</h4>""")
def test_regression_contract_api_log_contract_type_name_and_migrated_flag_false(setup):
        try:
                happy_path("ContractTypeNameAndMigratedFlagFalseTemplate.json")
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)

@allure.title("Umr is repeated and it has preveious error")
@allure.description_html("""<h4>This test is to verify that contract have errors on tide</h4>""")
def test_regression_umr_repeated_with_existing_error(setup):
        try:
                error_text = "L003: L003: Invalid DCOM Contract; Unable to load contract into TIDE.; Unable to load contract into TIDE."
                error_path("UmrRepeatedWithExistingErrorTemplate.json", error_text,Identifiers.UMR)
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)

@allure.title("Contract without contract currency")
@allure.description_html("""<h4>This test is to verify that contract have errors on tide</h4>""")
def test_regression_contract_api_log_contrac_wWithout_contract_currency(setup):
        try:
                error_text = "L003: Invalid DCOM Contract; Unable to load contract into TIDE."
                error_path("ContractWithoutContractCurrencyTemplate.json", error_text,Identifiers.UMR)
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)

@allure.title("ContractStatusName is equal to Registered")
@allure.description_html("""<h4>This test is to verify that contract does not have errors on tide</h4>""")
def test_regression_contract_api_log_contract_status_name_equal_registered(setup):
        try:
                happy_path("ContractStatusNameEqualRegisteredTemplate.json")
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)


@allure.title("MigratedFlag True & IsMigratedDraft True")
@allure.description_html("""<h4>This test is to verify that contract does not have errors on tide</h4>""")
def test_regression_contract_api_log_migrated_flag_true_and_is_migrated_draft_true(setup):
        try:
              happy_path("MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json")
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)

@allure.title("Umr & lcr are equal")
@allure.description_html("""<h4>This test is to verify that contract does not have errors on tide</h4>""")
def test_regression_contract_api_log_contract_with_same_umr_and_lcr(setup):
        try:
                happy_path('ContractWithSameUmrAndLcrTemplate.json')
        except Exception as ex:
                allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=AttachmentType.PNG)
                pytest.fail(str(ex), False)


def happy_path(file):
        t = open("./Data/SendJson/Templates/"+ file)
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Loaded_into_tide(umr, Identifiers.UMR)
        contratApiLogPage.click_check_btn(umr)
        contratApiLogPage.click_filter_btn()
        assert contratApiLogPage.read_status() =="-"

def error_path(file, error, search_by = Identifiers.UMR ):
        t = open("./Data/SendJson/Templates/"+ file)
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        lcr = dataTemplate['LloydsContractRef']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.click_contract_link()

        contractPage = ContractPage(driver)
        contractPage.click_contract_api_log_btn()

        contratApiLogPage = ContratApiLogPage(driver)
        if search_by == Identifiers.UMR:
                contratApiLogPage.wait_until_contract_is_Loaded_into_tide(umr, Identifiers.UMR)
                contratApiLogPage.click_check_btn(umr)
        elif search_by == Identifiers.LCR:
                contratApiLogPage.wait_until_contract_is_Loaded_into_tide(lcr, Identifiers.LCR)
                contratApiLogPage.click_check_btn(lcr)
        contratApiLogPage.click_filter_btn()
        contratApiLogPage.click_review_errors_btn()
        assert error in contratApiLogPage.read_errors(0)
        contratApiLogPage.click_ok_btn()
    

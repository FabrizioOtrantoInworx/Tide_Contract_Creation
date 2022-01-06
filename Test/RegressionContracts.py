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
    driver = WebDriver.Start_Driver()
    loginPage = LoginPage(driver)
    loginPage.Login()
    yield
    driver.close()

def test_RegressionContratApiLogTestVersionUpdateDateEqualCurrentDataTime(setup):
        t = open('./Data/SendJson/Templates/VersionUpdateDateEqualCurrentDataTimeTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.wait_until_contract_is_Load_into_tide(umr)
        contratApiLogPage.ClickUMRFilterBtn()
        contratApiLogPage.writeinSearchField(umr)
        contratApiLogPage.ClickCheckBtn(umr)
        contratApiLogPage.ClickFilterBtn()
        assert contratApiLogPage.readStatus() =="-"
        homePage.Navbar.ClickTideLogo()


def test_RegressionContratApiLogTestContractWihoutUMR(setup):
        t = open('./Data/SendJson/Templates/ContractWihoutUMRTemplate.json')
        dataTemplate = json.load (t)
        ssr = dataTemplate['LloydsContractRef']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.ClickSSRFilterBtn()
        contratApiLogPage.writeinSearchField(ssr)
        contratApiLogPage.ClickCheckBtn(ssr)
        contratApiLogPage.ClickFilterBtn()
        contratApiLogPage.ClickReviewErrorsBtn()
        assert contratApiLogPage.readErrors(0) == f"E004: UMR missing from contract; CONTRACTUMRISEMPTY; Contract with LloydsContractRef {ssr} does not have a valid UMR"
        contratApiLogPage.ClickOkBtn()
        homePage.Navbar.ClickTideLogo()

def test_RegressionContratApiLogTestContractWihoutLCR(setup):
        t = open('./Data/SendJson/Templates/ContractWihoutLCRTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.ClickUMRFilterBtn()
        contratApiLogPage.writeinSearchField(umr)
        contratApiLogPage.ClickCheckBtn(umr)
        contratApiLogPage.ClickFilterBtn()
        contratApiLogPage.ClickReviewErrorsBtn()
        assert contratApiLogPage.readErrors(0) == f"E003: LloydsContractRef missing from contract; CONTRACTLLOYDSCONTRACTREFISEMPTY; Contract with UMR {umr} does not have a valid Lloyds Contract Ref"
        contratApiLogPage.ClickOkBtn()
        homePage.Navbar.ClickTideLogo()

def test_RegressionContratApiLogTestContractStatusNameAndContractTypeName(setup):
        t = open('./Data/SendJson/Templates/ContractStatusNameAndContractTypeNameTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.ClickUMRFilterBtn()
        contratApiLogPage.writeinSearchField(umr)
        contratApiLogPage.ClickCheckBtn(umr)
        contratApiLogPage.ClickFilterBtn()
        assert contratApiLogPage.readStatus() =="-"
        homePage.Navbar.ClickTideLogo()


def test_RegressionContratApiLogTestContractTypeNameAndMigratedFlagMissing(setup):
        t = open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagMissingTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.ClickUMRFilterBtn()
        contratApiLogPage.writeinSearchField(umr)
        contratApiLogPage.ClickCheckBtn(umr)
        contratApiLogPage.ClickFilterBtn()
        assert contratApiLogPage.readStatus() =="-"
        homePage.Navbar.ClickTideLogo()

def test_RegressionContratApiLogTestContractTypeNameAndMigratedFlagFalse(setup):
        t = open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagFalseTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.ClickUMRFilterBtn()
        contratApiLogPage.writeinSearchField(umr)
        contratApiLogPage.ClickCheckBtn(umr)
        contratApiLogPage.ClickFilterBtn()
        assert contratApiLogPage.readStatus() =="-"
        homePage.Navbar.ClickTideLogo()


def test_RegressionContratApiLogTestContractWithoutContractCurrency(setup):
        t = open('./Data/SendJson/Templates/ContractWithoutContractCurrencyTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.ClickUMRFilterBtn()
        contratApiLogPage.writeinSearchField(umr)
        contratApiLogPage.ClickCheckBtn(umr)
        contratApiLogPage.ClickFilterBtn()
        contratApiLogPage.ClickReviewErrorsBtn()
        assert contratApiLogPage.readErrors(0) == "L003: Invalid DCOM Contract; Unable to load contract into TIDE."
        contratApiLogPage.ClickOkBtn()
        homePage.Navbar.ClickTideLogo()

def test_RegressionContratApiLogTestContractStatusNameEqualRegistered(setup):

        t = open('./Data/SendJson/Templates/ContractStatusNameEqualRegisteredTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.ClickUMRFilterBtn()
        contratApiLogPage.writeinSearchField(umr)
        contratApiLogPage.ClickCheckBtn(umr)
        contratApiLogPage.ClickFilterBtn()
        assert contratApiLogPage.readStatus() =="-"
        homePage.Navbar.ClickTideLogo()



def test_RegressionContratApiLogTestMigratedFlagTrueAndIsMigratedDraftTrue(setup):
        t = open('./Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.ClickUMRFilterBtn()
        contratApiLogPage.writeinSearchField(umr)
        contratApiLogPage.ClickCheckBtn(umr)
        contratApiLogPage.ClickFilterBtn()
        assert contratApiLogPage.readStatus() =="-"
        homePage.Navbar.ClickTideLogo()

def test_RegressionContratApiLogTestContractWithSameUmrAndLcr(setup):
        t = open('./Data/SendJson/Templates/ContractWithSameUmrAndLcrTemplate.json')
        dataTemplate = json.load (t)
        umr = dataTemplate['UMR']
        t.close()
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickContractApiLogBtn()

        contratApiLogPage = ContratApiLogPage(driver)
        contratApiLogPage.ClickUMRFilterBtn()
        contratApiLogPage.writeinSearchField(umr)
        contratApiLogPage.ClickCheckBtn(umr)
        contratApiLogPage.ClickFilterBtn()
        assert contratApiLogPage.readStatus() =="-"
        homePage.Navbar.ClickTideLogo()



def RegressionAddContract():
    try:
        homePage = HomePage(driver)
        homePage.Navbar.ClickContractLink()

        contractPage = ContractPage(driver)
        contractPage.ClickAddContractBtn()

        addContractPage = AddContractPage(driver)
        addContractPage.ClickAddFolderBtn()
        addContractPage.SelectFoldertype("Binder")
        addContractPage.SelectDivision("AT_Test Insurer 1 - Schedule Service")
        addContractPage.ClickSaveBtn()
        addContractPage.WriteUmr("aaa")
        addContractPage.SelectCurrency("ars")
        
    except Exception as ex:
        print(ex)
    

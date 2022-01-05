from Pages.LoginPage import LoginPage
from Pages.ContractPage import ContractPage
from Pages.HomePage import HomePage
from Pages.ContratApiLogPage import ContratApiLogPage
from Pages.AddContractPage import AddContractPage
from Core.WebDriver import WebDriver
import json
from unittest import IsolatedAsyncioTestCase


class RegressionContracts(IsolatedAsyncioTestCase):
        
    def RegressionContracts(self): 
          
        driver = WebDriver.Start_Driver()
        loginPage = LoginPage(driver)
        loginPage.Login()
        
        self.RegressionContratApiLogTestVersionUpdateDateEqualCurrentDataTime(driver)
        self.RegressionContratApiLogTestContractWihoutUMR(driver)
        self.RegressionContratApiLogTestContractWihoutLCR(driver)
        self.RegressionContratApiLogTestContractStatusNameAndContractTypeName(driver)
        self.RegressionContratApiLogTestContractTypeNameAndMigratedFlagMissing(driver)
        self.RegressionContratApiLogTestContractTypeNameAndMigratedFlagFalse(driver)
        self.RegressionContratApiLogTestContractWithoutContractCurrency(driver)
        self.RegressionContratApiLogTestContractStatusNameEqualRegistered(driver)
        self.RegressionContratApiLogTestMigratedFlagTrueAndIsMigratedDraftTrue(driver)
        self.RegressionContratApiLogTestContractWithSameUmrAndLcr(driver)
        
        
        #self.RegressionAddContract(driver)


        driver.close()

    def RegressionContratApiLogTestVersionUpdateDateEqualCurrentDataTime(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/VersionUpdateDateEqualCurrentDataTimeTemplate.json')
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
            self.assertEqual(contratApiLogPage.readStatus(), "-", "Test has not been successful")
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)

    def RegressionContratApiLogTestContractWihoutUMR(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWihoutUMRTemplate.json')
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
            self.assertIn("UMR missing from contract", contratApiLogPage.readErrors(0), "error not found")
            contratApiLogPage.ClickOkBtn()
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)

    def RegressionContratApiLogTestContractWihoutLCR(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWihoutLCRTemplate.json')
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
            self.assertIn("LloydsContractRef missing from contract", contratApiLogPage.readErrors(0), "error not found")
            contratApiLogPage.ClickOkBtn()
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)

    def RegressionContratApiLogTestContractStatusNameAndContractTypeName(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractStatusNameAndContractTypeNameTemplate.json')
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
            self.assertEqual(contratApiLogPage.readStatus(), "-", "Test has not been successful")
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)

    def RegressionContratApiLogTestContractTypeNameAndMigratedFlagMissing(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameAndMigratedFlagMissingTemplate.json')
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
            self.assertEqual(contratApiLogPage.readStatus(), "-", "Test has not been successful")
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)

    def RegressionContratApiLogTestContractTypeNameAndMigratedFlagFalse(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameAndMigratedFlagFalseTemplate.json')
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
            self.assertEqual(contratApiLogPage.readStatus(), "-", "Test has not been successful")
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)

    def RegressionContratApiLogTestContractWithoutContractCurrency(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithoutContractCurrencyTemplate.json')
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
            self.assertEqual(contratApiLogPage.readErrors(0),"L003: Invalid DCOM Contract; Unable to load contract into TIDE.", "error not found")
            contratApiLogPage.ClickOkBtn()
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)

    def RegressionContratApiLogTestContractStatusNameEqualRegistered(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractStatusNameEqualRegisteredTemplate.json')
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
            self.assertEqual(contratApiLogPage.readStatus(), "-", "Test has not been successful")
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)


    def RegressionContratApiLogTestMigratedFlagTrueAndIsMigratedDraftTrue(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json')
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
            self.assertEqual(contratApiLogPage.readStatus(), "-", "Test has not been successful")
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)

    def RegressionContratApiLogTestContractWithSameUmrAndLcr(self, driver):
        try:
            t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithSameUmrAndLcrTemplate.json')
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
            self.assertEqual(contratApiLogPage.readStatus(), "-", "Test has not been successful")
            homePage.Navbar.ClickTideLogo()
        except Exception as ex:
            print(ex)


    def RegressionAddContract(self, driver):
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
        

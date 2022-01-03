from Pages.LoginPage import LoginPage
from Pages.ContractPage import ContractPage
from Pages.HomePage import HomePage
from Pages.ContratApiLogPage import ContratApiLogPage
from Pages.AddContractPage import AddContractPage
from Core.WebDriver import WebDriver

class RegressionContracts:
        
    def RegressionContracts(self): 
          
        driver = WebDriver.Start_Driver()
        loginPage = LoginPage(driver)
        loginPage.Login()
        
        self.RegressionContratApiLogTestFailed(driver)
        self.RegressionAddContract(driver)

        driver.close()

    def RegressionContratApiLogTestFailed(self, driver):
        try:
            homePage = HomePage(driver)
            homePage.Navbar.ClickContractLink()

            contractPage = ContractPage(driver)
            contractPage.ClickContractApiLogBtn()

            contratApiLogPage = ContratApiLogPage(driver)
            contratApiLogPage.ClickUMRFilterBtn()
            contratApiLogPage.writeUMR()
            contratApiLogPage.ClickCheckBtn()
            contratApiLogPage.ClickFilterBtn()
            contratApiLogPage.ClickReviewErrorsBtn()
            contratApiLogPage.assertErrors()
            contratApiLogPage.ClickOkBtn()
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
        

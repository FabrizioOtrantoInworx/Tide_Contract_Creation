from selenium import webdriver
from Class_Methods import sendkeys_and_click, clicks, select_dropdown, wait_generic

# region Loginn

driver = webdriver.Chrome(executable_path='C:/Desarrollo/Python Scripts/Tide_Contract_Creation/Drivers/chromedriver.exe')
urlpath = "https://lt-d-tde-01-wa-01.azurewebsites.net/topmenu/contractlist"
driver.get(urlpath)

wait_generic(driver, "idSIButton9")
sendkeys_and_click(driver, "i0116", "DUP.Insurer1@ctplc.com", "idSIButton9")

wait_generic(driver, "submitButton")
sendkeys_and_click(driver, "passwordInput", "Tr4f4lg4$q.", "submitButton")

wait_generic(driver, "idSIButton9")
clicks(driver, "idSIButton9")
# endregion

wait_generic(driver, "btn_contractList_addContract")
clicks(driver, "btn_contractList_addContract")

wait_generic(driver, "btn_createContract_addFolder")
clicks(driver, "btn_createContract_addFolder")

wait_generic(driver, "k-6fee9b7b-1713-441c-9d55-18b0e58ec1a0")
#clicks(driver, "k-6fee9b7b-1713-441c-9d55-18b0e58ec1a0")

print("listo")

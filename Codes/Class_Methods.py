from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select #para seleccionar los combobox


def wait_generic(driverM, idM):
    try:
        WebDriverWait(driverM, 5).until(EC.presence_of_element_located((By.ID, idM)))
    except TimeoutException:
        print("Timed out waiting for page to load")


def sendkeys_and_click(driverM, elemNameM, elemKeysM, botonIDM):
    elem = driverM.find_element_by_id(elemNameM)
    elem.clear()
    elem.send_keys(elemKeysM)
    boton = driverM.find_element_by_id(botonIDM)
    boton.click()


def clicks(driverM, idM):
    boton = driverM.find_element_by_id(idM)
    boton.click()


def select_dropdown(driverM, listadoM, valueM):
    combo = driverM.find_element_by_id(listadoM)
    combo.click()

    
print("cambios en NUEVA BRANCH otro cambio!!")
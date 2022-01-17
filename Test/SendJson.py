import json
import datetime
import requests
from Core.Utilidades.Utilidades import Utilidades
import Data.SendJson.Properties as Properties
import pytest

            
def test_PastVersionUpadte():
    t = open('.//Data/SendJson/Templates/PastVersionUpdateTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestUno")
    UpdateVersionTime = dataTemplate['VersionUpdatedDate']
    UpdateVersionTimeCutted = UpdateVersionTime[0:19]
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/PastVersionUpdateTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/PastVersionUpdateTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 400
    assert r.reason =='Bad Request'
    assert UpdateVersionTimeCutted in r.text         

def test_FutureVersionUpadte():
    t = open('./Data/SendJson/Templates/FutureVersionUpdateTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestDos")
    UpdateVersionTime = dataTemplate['VersionUpdatedDate']
    UpdateVersionTimeCutted = UpdateVersionTime[0:19]
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/FutureVersionUpdateTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('.//Data/SendJson/Templates/FutureVersionUpdateTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 400
    assert r.reason =='Bad Request'
    assert UpdateVersionTimeCutted in r.text         

def test_VersionUpdateDateEqualCurrentDataTime():  
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/VersionUpdateDateEqualCurrentDataTimeTemplate.json')
    dataTemplate = json.load (t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestTres")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/VersionUpdateDateEqualCurrentDataTimeTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/VersionUpdateDateEqualCurrentDataTimeTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "VersionUpdateDateEqualCurrentDataTimeTemplate.json was successfully uploaded" in r.text

def test_ContractWihoutUMR():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/ContractWihoutUMRTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractWihoutUMRTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractWihoutUMRTemplate.json', 'rb')},headers=headers) 
    print (r)
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractWihoutUMRTemplate.json was successfully uploaded" in r.text

def test_ContractWihoutLCR():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')    
    t = open('./Data/SendJson/Templates/ContractWihoutLCRTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['UMR'] = Utilidades.CreateUMR("testCinco")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractWihoutLCRTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractWihoutLCRTemplate.json', 'rb')},headers=headers) 
    print (r)
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractWihoutLCRTemplate.json was successfully uploaded" in r.text

def test_ContractTypeNameWithoutContractSectionStatus():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/ContractTypeNameWithoutContractSectionStatusTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("testSeis")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractTypeNameWithoutContractSectionStatusTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractTypeNameWithoutContractSectionStatusTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractTypeNameWithoutContractSectionStatusTemplate.json was successfully uploaded" in r.text

def test_RepeatedUmrAndLcr():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/RepeatedUmrAndLcrTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = "LCRAlreadyExisting"
    dataTemplate['UMR'] = "UMRAlreadyExisting"
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/RepeatedUmrAndLcrTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/RepeatedUmrAndLcrTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "RepeatedUmrAndLcrTemplate.json was successfully uploaded" in r.text

def test_ContractStatusNameAndContractTypeName():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/ContractStatusNameAndContractTypeNameTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestOcho")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractStatusNameAndContractTypeNameTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractStatusNameAndContractTypeNameTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractStatusNameAndContractTypeNameTemplate.json was successfully uploaded" in r.text
    
def test_ContractTypeNameAndMigratedFlagMissing():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagMissingTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestNueve")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagMissingTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagMissingTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractTypeNameAndMigratedFlagMissingTemplate.json was successfully uploaded" in r.text

def test_ContractTypeNameAndMigratedFlagFalse():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagFalseTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestDiez")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagFalseTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractTypeNameAndMigratedFlagFalseTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractTypeNameAndMigratedFlagFalseTemplate.json was successfully uploaded" in r.text

def test_MigratedFlagTrueAndIsMigratedDraftFalse():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestOnce")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json was successfully uploaded" in r.text

def test_UmrRepeatedWithExistingError():

    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/UmrRepeatedWithExistingErrorTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/UmrRepeatedWithExistingErrorTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/UmrRepeatedWithExistingErrorTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "UmrRepeatedWithExistingErrorTemplate.json was successfully uploaded" in r.text

def test_InvalidCurrency():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/InvalidCurrencyTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestTrece")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/InvalidCurrencyTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/InvalidCurrencyTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "InvalidCurrencyTemplate.json was successfully uploaded" in r.text

def test_ContractWithoutContractCurrency():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/ContractWithoutContractCurrencyTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestQuince")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractWithoutContractCurrencyTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractWithoutContractCurrencyTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractWithoutContractCurrencyTemplate.json was successfully uploaded" in r.text

def test_ContractStatusNameEqualRegistered():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/ContractStatusNameEqualRegisteredTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestDieciseis")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractStatusNameEqualRegisteredTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractStatusNameEqualRegisteredTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractStatusNameEqualRegisteredTemplate.json was successfully uploaded" in r.text

def test_MigratedFlagTrueAndIsMigratedDraftTrue():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    dataTemplate['UMR'] = Utilidades.CreateUMR("TestDiecisiete")
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json was successfully uploaded" in r.text

def test_ContractWithoutContra2ctStatus():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/ContractWithoutContra2ctStatusTemplate.json')
    dataTemplate = json.load(t)
    dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
    umr = Utilidades.CreateUMR("TestDieciocho")
    dataTemplate['UMR'] = umr
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractWithoutContra2ctStatusTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractWithoutContra2ctStatusTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractWithoutContra2ctStatusTemplate.json was successfully uploaded" in r.text

def test_ContractWithSameUmrAndLcr():
    utcnow = datetime.datetime.utcnow()
    utc_now_fixed = utcnow - datetime.timedelta(seconds=10)
    NVUD = utc_now_fixed.strftime('%Y-%m-%dT%H:%M:%S.000Z')
    t = open('./Data/SendJson/Templates/ContractWithSameUmrAndLcrTemplate.json')
    dataTemplate = json.load(t)
    umrAndLcr = Utilidades.CreateUMR("TestDiecinueve")
    dataTemplate['LloydsContractRef'] = umrAndLcr
    dataTemplate['UMR'] = umrAndLcr
    dataTemplate['VersionUpdatedDate'] = NVUD
    data = json.dumps(dataTemplate)
    writableFile = open('./Data/SendJson/Templates/ContractWithSameUmrAndLcrTemplate.json','w')
    writableFile.write(data)
    writableFile.close()
    t.close()
    url = Properties.Url
    headers = Properties.Header
    r =  requests.post(url, files={'file': open('./Data/SendJson/Templates/ContractWithSameUmrAndLcrTemplate.json', 'rb')},headers=headers) 
    assert r.status_code == 200
    assert r.reason =='OK'
    assert "ContractWithSameUmrAndLcrTemplate.json was successfully uploaded" in r.text

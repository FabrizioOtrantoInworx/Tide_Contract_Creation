import json
import datetime
import requests
from Core.Utilidades.Utilidades import Utilidades
import Data.SendJson.Properties as Properties
from unittest import IsolatedAsyncioTestCase

class TestSendJson(IsolatedAsyncioTestCase):
        
    def RegresionSendJson(self): 
        
        self.TestPastVersionUpadte() #Works
        self.TestFutureVersionUpadte() #Works
        self.TestVersionUpdateDateEqualCurrentDataTime() #works
        self.TestContractWihoutUMR() #works
        self.TestContractWihoutLCR() #works
        self.TestContractTypeNameWithoutContractSectionStatus() #does not work
        self.TestRepeatedUmrAndLcr() #does not work Checkear en DB
        self.TestContractStatusNameAndContractTypeName() #works
        self.TestContractTypeNameAndMigratedFlagMissing() #works
        self.TestContractTypeNameAndMigratedFlagFalse() #works
        self.TestMigratedFlagTrueAndIsMigratedDraftFalse() #does not works Checkear en DB
        self.TestUmrRepeatedWithExistingError() #does not works checkear en DB
        self.TestInvalidCurrency() #does not works / Llega a tide pero no cambia la moneda
        self.TestContractWithoutContractCurrency() #works
        self.TestContractStatusNameEqualRegistered() #works
        self.TestMigratedFlagTrueAndIsMigratedDraftTrue() #works
        self.TestContractWithoutContra2ctStatus() #does not works  / no llega a Tide
        self.TestContractWithSameUmrAndLcr() #works 
        
    def TestPastVersionUpadte(self):
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/PastVersionUpdateTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestUno")
        UpdateVersionTime = dataTemplate['VersionUpdatedDate']
        UpdateVersionTimeCutted = UpdateVersionTime[0:19]
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/PastVersionUpdateTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/PastVersionUpdateTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 400, 'Bad request was not the reason')
        self.assertEqual(r.reason,'Bad Request', "Bad request was not the reason")
        self.assertIn(UpdateVersionTimeCutted, r.text, "Update version time is not in the response text")        

    def TestFutureVersionUpadte(self):
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/FutureVersionUpdateTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestDos")
        UpdateVersionTime = dataTemplate['VersionUpdatedDate']
        UpdateVersionTimeCutted = UpdateVersionTime[0:19]
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/FutureVersionUpdateTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/FutureVersionUpdateTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 400, 'Bad request was not the reason')
        self.assertEqual(r.reason,'Bad Request', "Bad request was not the reason")
        self.assertIn(UpdateVersionTimeCutted, r.text, "Update version time is not in the response text")        

    def TestVersionUpdateDateEqualCurrentDataTime(self):  
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/VersionUpdateDateEqualCurrentDataTimeTemplate.json')
        dataTemplate = json.load (t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestTres")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/VersionUpdateDateEqualCurrentDataTimeTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/VersionUpdateDateEqualCurrentDataTimeTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("VersionUpdateDateEqualCurrentDataTimeTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestContractWihoutUMR(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWihoutUMRTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWihoutUMRTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWihoutUMRTemplate.json', 'rb')},headers=headers) 
        print (r)
        self.assertEqual(r.status_code, 200, 'Contract has not been created')
        self.assertEqual(r.reason,'OK', "Contract was not created")
        self.assertIn("ContractWihoutUMRTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestContractWihoutLCR(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWihoutLCRTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['UMR'] = Utilidades.CreateUMR("testCinco")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWihoutLCRTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWihoutLCRTemplate.json', 'rb')},headers=headers) 
        print (r)
        self.assertEqual(r.status_code, 200, 'Contract has not been created')
        self.assertEqual(r.reason,'OK', "Contract was not created")
        self.assertIn("ContractWihoutLCRTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestContractTypeNameWithoutContractSectionStatus(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameWithoutContractSectionStatusTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("testSeis")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameWithoutContractSectionStatusTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameWithoutContractSectionStatusTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("ContractTypeNameWithoutContractSectionStatusTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestRepeatedUmrAndLcr(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/RepeatedUmrAndLcrTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = "LCRAlreadyExisting"
        dataTemplate['UMR'] = "UMRAlreadyExisting"
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/RepeatedUmrAndLcrTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/RepeatedUmrAndLcrTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("RepeatedUmrAndLcrTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestContractStatusNameAndContractTypeName(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractStatusNameAndContractTypeNameTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestOcho")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractStatusNameAndContractTypeNameTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractStatusNameAndContractTypeNameTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("ContractStatusNameAndContractTypeNameTemplate.json was successfully uploaded", r.text,"contract has not been created")
       
    def TestContractTypeNameAndMigratedFlagMissing(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameAndMigratedFlagMissingTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestNueve")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameAndMigratedFlagMissingTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameAndMigratedFlagMissingTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("ContractTypeNameAndMigratedFlagMissingTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestContractTypeNameAndMigratedFlagFalse(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameAndMigratedFlagFalseTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestDiez")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameAndMigratedFlagFalseTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractTypeNameAndMigratedFlagFalseTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("ContractTypeNameAndMigratedFlagFalseTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestMigratedFlagTrueAndIsMigratedDraftFalse(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestOnce")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestUmrRepeatedWithExistingError(self):

        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/UmrRepeatedWithExistingErrorTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/UmrRepeatedWithExistingErrorTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/UmrRepeatedWithExistingErrorTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("UmrRepeatedWithExistingErrorTemplate.json was successfully uploaded", r.text,"contract has not been created")
  
    def TestInvalidCurrency(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/InvalidCurrencyTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestTrece")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/InvalidCurrencyTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/InvalidCurrencyTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("InvalidCurrencyTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestContractWithoutContractCurrency(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithoutContractCurrencyTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestQuince")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithoutContractCurrencyTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithoutContractCurrencyTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("ContractWithoutContractCurrencyTemplate.json was successfully uploaded", r.text,"contract has not been created")
    
    def TestContractStatusNameEqualRegistered(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractStatusNameEqualRegisteredTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestDieciseis")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractStatusNameEqualRegisteredTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractStatusNameEqualRegisteredTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("ContractStatusNameEqualRegisteredTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestMigratedFlagTrueAndIsMigratedDraftTrue(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestDiecisiete")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestContractWithoutContra2ctStatus(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithoutContra2ctStatusTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        umr = Utilidades.CreateUMR("TestDieciocho")
        dataTemplate['UMR'] = umr
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithoutContra2ctStatusTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithoutContra2ctStatusTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("ContractWithoutContra2ctStatusTemplate.json was successfully uploaded", r.text,"contract has not been created")

    def TestContractWithSameUmrAndLcr(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithSameUmrAndLcrTemplate.json')
        dataTemplate = json.load(t)
        umrAndLcr = Utilidades.CreateUMR("TestDiecinueve")
        dataTemplate['LloydsContractRef'] = umrAndLcr
        dataTemplate['UMR'] = umrAndLcr
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithSameUmrAndLcrTemplate.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/ContractWithSameUmrAndLcrTemplate.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("ContractWithSameUmrAndLcrTemplate.json was successfully uploaded", r.text,"contract has not been created")
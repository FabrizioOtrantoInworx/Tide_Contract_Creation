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
        self.Test4NoUMR() #works
        self.Test5NoLCR() #works
        self.Test6() #does not work
        self.Test7() #does not work
        self.Test8() #works
        self.Test9() #works
        self.Test10() #works
        self.Test11() #does not works
        self.Test12() #does not works
        self.Test13() #does not works / Llega a tide pero no cambia la moneda
        self.Test15() #works
        self.Test16() #works
        self.Test17() #works
        self.Test18() #does not works  / no llega a Tide
        self.Test19() #works 
        
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
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test3.json')
        dataTemplate = json.load (t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestTres")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test3.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test3.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test3.json was successfully uploaded", r.text,"contract has not been created")

    def Test4NoUMR(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test4.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test4.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test4.json', 'rb')},headers=headers) 
        print (r)
        self.assertEqual(r.status_code, 200, 'Contract has not been created')
        self.assertEqual(r.reason,'OK', "Contract was not created")
        self.assertIn("Test4.json was successfully uploaded", r.text,"contract has not been created")

    def Test5NoLCR(self):
        now = datetime.datetime.now()
        #NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test5.json')
        dataTemplate = json.load(t)
        dataTemplate['UMR'] = Utilidades.CreateUMR("testCinco")
        #dataTemplate['VersionUpdatedDate'] = NVUD
        #dataTemplate['ContractSections']['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test5.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test5.json', 'rb')},headers=headers) 
        print (r)
        self.assertEqual(r.status_code, 200, 'Contract has not been created')
        self.assertEqual(r.reason,'OK', "Contract was not created")
        self.assertIn("Test5.json was successfully uploaded", r.text,"contract has not been created")

    def Test6(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test6.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("testSeis")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test6.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test6.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test6.json was successfully uploaded", r.text,"contract has not been created")

    def Test7(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test7.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = "LCRAlreadyExisting"
        dataTemplate['UMR'] = "UMRAlreadyExisting"
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test7.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test7.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test7.json was successfully uploaded", r.text,"contract has not been created")

    def Test8(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test8.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestOcho")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test8.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test8.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test8.json was successfully uploaded", r.text,"contract has not been created")
       
    def Test9(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test9.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestNueve")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test9.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test9.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test9.json was successfully uploaded", r.text,"contract has not been created")

    def Test10(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test10.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestDiez")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test10.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test10.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test10.json was successfully uploaded", r.text,"contract has not been created")

    def Test11(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test11.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestOnce")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test11.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test11.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test11.json was successfully uploaded", r.text,"contract has not been created")

    def Test12(self):

        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test12.json')
        dataTemplate = json.load(t)
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test12.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test12.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test12.json was successfully uploaded", r.text,"contract has not been created")
  
    def Test13(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test13.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestTrece")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test13.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test13.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test13.json was successfully uploaded", r.text,"contract has not been created")

    def Test15(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test15.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestQuince")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test15.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test15.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test15.json was successfully uploaded", r.text,"contract has not been created")
    
    def Test16(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test16.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestDieciseis")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test16.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test16.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test16.json was successfully uploaded", r.text,"contract has not been created")

    def Test17(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test17.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR("TestDiecisiete")
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test17.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test17.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test17.json was successfully uploaded", r.text,"contract has not been created")

    def Test18(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test18.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        umr = Utilidades.CreateUMR("TestDieciocho")
        dataTemplate['UMR'] = umr
        print(umr)
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test18.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test18.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test18.json was successfully uploaded", r.text,"contract has not been created")

    def Test19(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test19.json')
        dataTemplate = json.load(t)
        umrAndLcr = Utilidades.CreateUMR("TestDiecinueve")
        dataTemplate['LloydsContractRef'] = umrAndLcr
        dataTemplate['UMR'] = umrAndLcr
        dataTemplate['VersionUpdatedDate'] = NVUD
        data = json.dumps(dataTemplate)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test19.json','w')
        writableFile.write(data)
        writableFile.close()
        t.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/Test19.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        self.assertIn("Test19.json was successfully uploaded", r.text,"contract has not been created")
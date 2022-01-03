import json
import datetime
import requests
from Core.Utilidades.Utilidades import Utilidades
import Data.SendJson.Properties as Properties
from unittest import IsolatedAsyncioTestCase

class TestSendJson(IsolatedAsyncioTestCase):
        
    def RegresionSendJson(self): 
        
        self.TestPastVersionUpadte()
        self.TestFutureVersionUpadte()
        self.TestVersionUpdateDateEqualCurrentDataTime()
        self.Test6()
        self.Test8()

    def TestPastVersionUpadte(self):
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/Templates/PastVersionUpdateTemplate.json')
        dataTemplate = json.load(t)
        dataTemplate['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        dataTemplate['UMR'] = Utilidades.CreateUMR()
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
        dataTemplate['UMR'] = Utilidades.CreateUMR()
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
       

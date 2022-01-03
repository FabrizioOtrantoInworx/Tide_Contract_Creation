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

    def TestPastVersionUpadte(self):
        f = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/PastVersionUpdateTemplate.json')
        dataTemplate = json.load(t)
        data = json.load (f)
        data['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        data['UMR'] = Utilidades.CreateUMR()
        data['VersionUpdatedDate'] = dataTemplate['VersionUpdatedDate']
        UpdateVersionTime = data['VersionUpdatedDate']
        UpdateVersionTimeCutted = UpdateVersionTime[0:19]
        data = json.dumps(data)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json','w')
        writableFile.write(data)
        writableFile.close()
        f.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/data.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 400, 'Bad request was not the reason')
        self.assertEqual(r.reason,'Bad Request', "Bad request was not the reason")
        self.assertIn(UpdateVersionTimeCutted, r.text, "Update version time is not in the response text")        


    def TestFutureVersionUpadte(self):
        f = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/FutureVersionUpdateTemplate.json')
        dataTemplate = json.load(t)
        data = json.load (f)
        data['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        data['UMR'] = Utilidades.CreateUMR()
        data['VersionUpdatedDate'] = dataTemplate['VersionUpdatedDate']
        UpdateVersionTime = data['VersionUpdatedDate']
        UpdateVersionTimeCutted = UpdateVersionTime[0:19]
        data = json.dumps(data)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json','w')
        writableFile.write(data)
        writableFile.close()
        f.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/data.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 400, 'Bad request was not the reason')
        self.assertEqual(r.reason,'Bad Request', "Bad request was not the reason")
        self.assertIn(UpdateVersionTimeCutted, r.text, "Update version time is not in the response text")        

    def TestVersionUpdateDateEqualCurrentDataTime(self):  
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        f = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json')
        data = json.load (f)
        data['LloydsContractRef'] = Utilidades.CreateSourceSystemReference()
        data['UMR'] = Utilidades.CreateUMR()
        data['VersionUpdatedDate'] = NVUD
        data = json.dumps(data)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json','w')
        writableFile.write(data)
        writableFile.close()
        f.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/data.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 200, 'contract has not been created')
        self.assertEqual(r.reason,'OK', "contract has not been created")
        


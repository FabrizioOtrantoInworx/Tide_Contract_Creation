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
        data['LloydsContractRef'] = Utilidades.CreateSourceSystemReference("Source")
        data['UMR'] = Utilidades.CreateUMR()
        data['VersionUpdatedDate'] = dataTemplate['VersionUpdatedDate']
        data = json.dumps(data)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json','w')
        writableFile.write(data)
        writableFile.close()
        f.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/data.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 400, 'contract has not been created')
        self.assertEqual(r.reason,'Bad Request', "contract has not been created")
        


    def TestFutureVersionUpadte(self):
        f = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/FutureVersionUpdateTemplate.json')
        dataTemplate = json.load(t)
        data = json.load (f)
        data['LloydsContractRef'] = Utilidades.CreateSourceSystemReference("Source")
        data['UMR'] = Utilidades.CreateUMR()
        data['VersionUpdatedDate'] = dataTemplate['VersionUpdatedDate']
        data = json.dumps(data)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json','w')
        writableFile.write(data)
        writableFile.close()
        f.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/data.json', 'rb')},headers=headers) 
        self.assertEqual(r.status_code, 400, 'contract has not been created')
        self.assertEqual(r.reason,'Bad Request', "contract has not been created")
        
        

    def TestVersionUpdateDateEqualCurrentDataTime(self):  
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        f = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/template.json')
        data = json.load (f)
        data['LloydsContractRef'] = Utilidades.CreateSourceSystemReference("Source")
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
        self.assertEqual(r.status_code, 200, 'contract has been created')
        self.assertEqual(r.reason,'OK', "contract has been created")
        


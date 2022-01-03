import json
import datetime
import requests
from Core.Utilidades.Utilidades import Utilidades
import Data.SendJson.Properties as Properties
from unittest import IsolatedAsyncioTestCase

class TestSendJson(IsolatedAsyncioTestCase):
        
    def RegresionSendJson(self): 
        
        self.sendJson()

    def sendJson(self):
        now = datetime.datetime.now()
        NVUD = now.strftime('%Y-%m-%dT%H:%M:%S.000Z')
        f = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json')
        t = open('C:/PythonAutomation/Scripts/Data/SendJson/template.json')
        dataTemplate = json.load(t)
        data = json.load (f)
        data['LloydsContractRef'] = Utilidades.CreateSourceSystemReference("Source")
        data['UMR'] = Utilidades.CreateUMR()
        if dataTemplate['VersionUpdatedDate'] is None:
            data['VersionUpdatedDate'] = NVUD
        else:
            data['VersionUpdatedDate'] = dataTemplate['VersionUpdatedDate']
        data = json.dumps(data)
        writableFile = open('C:/PythonAutomation/Scripts/Data/SendJson/data.json','w')
        writableFile.write(data)
        writableFile.close()
        f.close()
        url = Properties.Url
        headers = Properties.Header
        r =  requests.post(url, files={'file': open('C:/PythonAutomation/Scripts/Data/SendJson/data.json', 'rb')},headers=headers) 
        print(r)
        



import json


class Configuration:
    
    def setBrowser():
        t= open ("C:/PythonAutomation/Scripts/Data/Appconfig.json")
        appConfig = json.load(t)
        browser = appConfig["browser"]
        return browser

    def setUrl():
        t= open ("C:/PythonAutomation/Scripts/Data/Appconfig.json")
        appConfig = json.load(t)
        url = appConfig["url"]
        return url

    def setRutaDriver():
        t= open ("C:/PythonAutomation/Scripts/Data/Appconfig.json")
        appConfig = json.load(t)
        rutaDriver = appConfig["rutaDriver"]
        return rutaDriver

    def setUsername():
        t= open ("C:/PythonAutomation/Scripts/Data/Appconfig.json")
        appConfig = json.load(t)
        username = appConfig["username"]
        return username

    def setPassword():
        t= open ("C:/PythonAutomation/Scripts/Data/Appconfig.json")
        appConfig = json.load(t)
        password = appConfig["password"]
        return password
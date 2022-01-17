import json


class Configuration:
    
    def set_browser():
        t= open ("./Data/Appconfig.json")
        appConfig = json.load(t)
        browser = appConfig["browser"]
        return browser

    def set_url():
        t= open ("./Data/Appconfig.json")
        appConfig = json.load(t)
        url = appConfig["url"]
        return url

    def set_ruta_driver():
        t= open ("./Data/Appconfig.json")
        appConfig = json.load(t)
        rutaDriver = appConfig["rutaDriver"]
        return rutaDriver

    def set_username():
        t= open ("./Data/Appconfig.json")
        appConfig = json.load(t)
        username = appConfig["username"]
        return username

    def set_password():
        t= open ("./Data/Appconfig.json")
        appConfig = json.load(t)
        password = appConfig["password"]
        return password
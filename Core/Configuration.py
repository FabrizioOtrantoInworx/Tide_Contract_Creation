import json
import Data.SendJson.Properties as Properties

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
        if appConfig['environment'] == "BETA":
            beta_username = appConfig["beta_username"]
            return beta_username
        elif appConfig['environment'] == "DEV":
            dev_username = appConfig["dev_username"]
            return dev_username
        elif appConfig['environment'] == "INT":
            int_username = appConfig["int_username"]
            return int_username
        

    def set_password():
        t= open ("./Data/Appconfig.json")
        appConfig = json.load(t)
        if appConfig['environment'] == "BETA":
            beta_password = appConfig["beta_password"]
            return beta_password
        elif appConfig['environment'] == "DEV":
            dev_password = appConfig["dev_password"]
            return dev_password
        elif appConfig['environment'] == "INT":
            int_password = appConfig["int_password"]
            return int_password

    
    def set_envirnment():
        t= open ("./Data/Appconfig.json")
        appConfig = json.load(t)
        environment = appConfig["environment"]
        return environment


    def set_url_for_json(enviroment):
        if enviroment == "BETA":
                url = Properties.beta_url
                return url
        elif enviroment == "DEV":
                url = Properties.dev_url
                return url
        elif enviroment == "INT":
                url = Properties.int_url
                return url

    def set_header_for_json(enviroment):
        if enviroment == "BETA":
                headers = Properties.beta_header
                return headers
        elif enviroment == "DEV":
                headers = Properties.dev_header
                return headers
        elif enviroment == "INT":
                headers = Properties.int_header
                return headers
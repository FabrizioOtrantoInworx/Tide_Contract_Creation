import tkinter as tk
from tkinter import END, ttk
import json

def main():
    root = tk.Tk()
    FrontApp(root, "Tide App", "400x400")


class FrontApp:
    def __init__(self, root, title, geometry):
        self.root = root
        self.root.title(title)
        self.root.geometry(geometry)
        self.root.grid_columnconfigure(2, minsize=40)

        self.username_label = tk.Label(self.root, text="Username", padx=20, pady=5)
        self.username_label.grid(row=3, column=1)
        self.username_input = tk.Entry(self.root)
        self.username_input.insert(0,"dev.admin@tideapp.co.uk")
        self.username_input.grid(row=3, column=3)

        self.password_label = tk.Label(self.root, text="Password", padx=20, pady=5)
        self.password_label.grid(row=4, column=1)
        self.password_input = tk.Entry(self.root)
        self.password_input.insert(0,"WdFV%.2431")
        self.password_input.grid(row=4, column=3)

        self.browser_label = tk.Label(self.root, text="Browser", padx=20, pady=5)
        self.browser_label.grid(row=5, column=1)
        self.browser_cmb = ttk.Combobox(self.root, values=["chrome", "firefox", "edge"])
        self.browser_cmb.current(0)
        self.browser_cmb.grid(row=5, column=3)

        self.route_driver_label = tk.Label(self.root, text="Route Driver", padx=20, pady=5)
        self.route_driver_label.grid(row=6, column=1)
        self.route_driver_input = tk.Entry(self.root)
        self.route_driver_input.insert(0,"C:/PythonAutomation/")
        self.route_driver_input.grid(row=6, column=3)

        self.environment_label = tk.Label(self.root, text="Environment", padx=20, pady=5)
        self.environment_label.grid(row=1, column=1)
        self.environment_cmb = ttk.Combobox(self.root, values = ["BETA", "DEV", "INT"])
        self.environment_cmb.current(0)
        self.environment_cmb.grid(row=1, column=3)

        self.umr_Label = tk.Label(self.root, text="UMR", padx=20, pady=5)
        self.umr_Label.grid(row=8, column=1)
        self.umr_Label = tk.Entry(self.root)
        self.umr_Label.grid(row=8, column=3)


        self.setEnviroment = tk.Button(self.root, text="Set Enviroment", command = self.set_environment, width=15, height=1)
        self.setEnviroment.grid(row=2, column=3)
        self.setChanges = tk.Button(self.root, text="Set Changes", command = self.set_new_app_config, width=15, height=1)
        self.setChanges.grid(row=9, column=3)
        self.stratTest = tk.Button(self.root, text="Start", command = self.root.destroy , width=15, height=1)
        self.stratTest.grid(row=10, column=3)

        self.root.mainloop()


    def set_environment(self):
        appConfigData= open ("./Data/Appconfig.json")
        appConfig = json.load(appConfigData)
        environment = self.environment_cmb.get()
        appConfig["environment"] = environment
        appConfig = json.dumps(appConfig)
        writableFile = open('./Data/Appconfig.json','w')
        writableFile.write(appConfig)
        writableFile.close()
        appConfigData.close()
        appConfigData2= open ("./Data/Appconfig.json")
        appConfig2 = json.load(appConfigData2)
        self.username_input.delete(0, END)
        self.password_input.delete(0, END)
        if self.environment_cmb.get() == "BETA":
            self.username_input.insert(0,appConfig2['beta_username'])
            self.password_input.insert(0,appConfig2['beta_password'])
        elif self.environment_cmb.get() == "DEV":
            self.username_input.insert(0,appConfig2['dev_username'])
            self.password_input.insert(0,appConfig2['dev_password'])
        elif self.environment_cmb.get() == "INT":
            self.username_input.insert(0,appConfig2['int_username'])
            self.password_input.insert(0,appConfig2['int_password'])
        appConfigData2.close()

    def set_new_app_config(self):
        appConfigData= open ("./Data/Appconfig.json")
        appConfig = json.load(appConfigData)
        username = self.username_input.get()
        password = self.password_input.get()
        browser = self.browser_cmb.get()
        driverRoute = self.route_driver_input.get()
        if self.environment_cmb.get() == "BETA":
            appConfig['beta_username'] = username
            appConfig['beta_password'] = password
        elif self.environment_cmb.get() == "DEV":
            appConfig['dev_username'] = username
            appConfig['dev_password'] = password
        elif self.environment_cmb.get() == "INT":
            appConfig['int_username'] = username
            appConfig['int_password'] = password
        appConfig["browser"] = browser
        appConfig["rutaDriver"] = driverRoute
        appConfig["url"] = self.set_url()
        appConfig = json.dumps(appConfig)
        writableFile = open('./Data/Appconfig.json','w')
        writableFile.write(appConfig)
        writableFile.close()
        appConfigData.close()

        contractonConfigData = open("./Data/Contracts/Contract_template.json")
        contractConfig = json.load(contractonConfigData)
        umr = self.umr_Label.get()
        contractConfig['contract']['umr'] = umr
        contractConfig = json.dumps(contractConfig)
        write_contract_config = open("./Data/Contracts/Contract_template.json",'w')
        write_contract_config.write(contractConfig)
        write_contract_config.close()
        write_contract_config.close()


    def set_url(self):
        if self.environment_cmb.get() == "INT":
            return "https://dasats.int.ctinsuretech.com/"
        elif self.environment_cmb.get() == "BETA":
            return "https://beta.tideapp.co.uk/"
        elif self.environment_cmb.get() == "DEV":
            return "https://lt-d-tde-01-wa-01.azurewebsites.net/home"
            

main()
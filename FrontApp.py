import tkinter as tk
from tkinter import ttk
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

        self.usernameLabel = tk.Label(self.root, text="Username", padx=20, pady=5)
        self.usernameLabel.grid(row=1, column=1)
        self.usernameInput = tk.Entry(self.root)
        self.usernameInput.insert(0,"dev.admin@tideapp.co.uk")
        self.usernameInput.grid(row=1, column=3)

        self.passwordLabel = tk.Label(self.root, text="Password", padx=20, pady=5)
        self.passwordLabel.grid(row=2, column=1)
        self.passwordInput = tk.Entry(self.root)
        self.passwordInput.insert(0,"WdFV%.2431")
        self.passwordInput.grid(row=2, column=3)

        self.browserLabel = tk.Label(self.root, text="Browser", padx=20, pady=5)
        self.browserLabel.grid(row=3, column=1)
        self.browserCmb = ttk.Combobox(self.root, values=["chrome", "firefox", "edge"])
        self.browserCmb.grid(row=3, column=3)

        self.routeDriverLabel = tk.Label(self.root, text="Route Driver", padx=20, pady=5)
        self.routeDriverLabel.grid(row=4, column=1)
        self.routeDriverInput = tk.Entry(self.root)
        self.routeDriverInput.insert(0,"C:/PythonAutomation/")
        self.routeDriverInput.grid(row=4, column=3)

        self.urlLabel = tk.Label(self.root, text="URL", padx=20, pady=5)
        self.urlLabel.grid(row=5, column=1)
        self.urlInput = ttk.Combobox(self.root, values = ["INT", "BETA"])
        self.urlInput.grid(row=5, column=3)

        self.umr_Label = tk.Label(self.root, text="UMR", padx=20, pady=5)
        self.umr_Label.grid(row=6, column=1)
        self.umr_Label = tk.Entry(self.root)
        self.umr_Label.grid(row=6, column=3)


        self.setChanges = tk.Button(self.root, text="Set Changes", command = self.set_new_app_config, width=15, height=1)
        self.setChanges.grid(row=7, column=3)
        self.stratTest = tk.Button(self.root, text="Start", command = self.root.destroy , width=15, height=1)
        self.stratTest.grid(row=8, column=3)

        self.root.mainloop()


    def set_new_app_config(self):
        appConfigData= open ("./Data/Appconfig.json")
        appConfig = json.load(appConfigData)
        username = self.usernameInput.get()
        password = self.passwordInput.get()
        browser = self.browserCmb.get()
        driverRoute = self.routeDriverInput.get()
        appConfig["username"] = username
        appConfig["password"] = password
        appConfig["browser"] = browser
        appConfig["rutaDriver"] = driverRoute
        appConfig["url"] = self.set_enviroment()
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


    def set_enviroment(self):
        if self.urlInput.get() == "INT":
            return "https://dasats.int.ctinsuretech.com/"
        elif self.urlInput.get() == "BETA":
            return "https://beta.tideapp.co.uk/"

main()
cd C:\TideAutomation\TIDE\PythonAutomation
python Frontapp.py
python -m py.test --alluredir=reports Test/SendJson.py -n 18
python -m py.test --alluredir=reports Test/RegressionContracts.py -n 4
allure serve reports
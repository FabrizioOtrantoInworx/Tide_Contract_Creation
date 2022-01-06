cd C:/PythonAutomation/Scripts
python Frontapp.py
python -m py.test --alluredir=reports Test/SendJson.py
python -m py.test --alluredir=reports Test/RegressionContracts.py
allure serve reports
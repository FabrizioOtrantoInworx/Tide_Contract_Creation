cd C:/PythonAutomation/Scripts
python Frontapp.py
python -m py.test --alluredir=reports Test/SendJson.py -n 18
python -m py.test --alluredir=reports Test/RegressionContracts.py -n 1
allure serve reports
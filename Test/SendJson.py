import json
import requests
from Core.Configuration import Configuration
from Core.Utilidades.Utilidades import Utilidades
import Data.SendJson.Properties as Properties
import pytest
import allure

# @allure.title("Past version Update Date")
# @allure.description_html("""<h4>This test is to verify that the contract is not being sent when 'version update' is set to an past date</h4>""")
# def test_past_version_update():
#     try:
#         data_time = "2021-12-29T13:13:25.000Z"
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("PastVersionUpdateTemplate.json", data_time, "", umr_code, lcr_code)
#         expected_status_code = 400
#         expectead_reason = "Bad Request"
#         expected_text = " within the file PastVersionUpdateTemplate.json does not lie in the date range"
#         assert r.status_code == expected_status_code
#         assert r.reason == expectead_reason
#         data_time_cutted = data_time[0:19]
#         assert data_time_cutted + expected_text in r.text
#     except Exception as ex:
#         pytest.fail(f"Test have failed.\n\n Status code:\n Expected: {expected_status_code} \n Actual: {r.status_code} \n\n Reason\n expected: {expectead_reason} \n actual: {r.reason} \n\n Text\n {r.text} \n\n excepcion: {ex}", False)    

# @allure.title("Future version Update Date")
# @allure.description_html("""<h4>This test is to verify that the contract is not being sent when 'version update' is set to a future date</h4>""")
# def test_future_version_update():
#     try:
#         data_time = "2022-12-29T13:13:25.000Z"
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("FutureVersionUpdateTemplate.json", data_time, "", umr_code, lcr_code)
#         assert r.status_code == 400
#         assert r.reason == "Bad Request"
#         data_time_cutted = data_time[0:19]
#         assert data_time_cutted + " within the file FutureVersionUpdateTemplate.json does not lie in the date range" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)    

# @allure.title("Current Version Update Date")
# @allure.description_html("""<h4>This test is to verify that the contract is being sent when 'version update' is set to current date</h4>""")
# def test_version_update_date_equal_current_data_time():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("VersionUpdateDateEqualCurrentDataTimeTemplate.json", data_time, "TestTres", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "VersionUpdateDateEqualCurrentDataTimeTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("Contract without umr")
# @allure.description_html("""<h4>This test is to verify that the contract is being sent when 'UMR' is set to null</h4>""")
# def test_contract_wihout_umr():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = ""
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("ContractWihoutUMRTemplate.json", data_time, "", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractWihoutUMRTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("Contract without lcr")
# @allure.description_html("""<h4>This test is to verify that the contract is being sent when 'LCR' is set to null</h4>""")
# def test_contract_wihout_lcr():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code = ""
#         r = send_valid_json("ContractWihoutLCRTemplate.json",data_time, "", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractWihoutLCRTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("ContractTpyeName equal to Cover holder appointment agreement & without contract section status")
# @allure.description_html("""<h4>This test is to verify that the contract is being sent when does not have contract section status</h4>""")
# def test_contract_type_name_without_contract_section_status():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("ContractTypeNameWithoutContractSectionStatusTemplate.json", data_time, "TestSeis",umr_code,lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractTypeNameWithoutContractSectionStatusTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

<<<<<<< HEAD
@allure.title("Repeated umr")
@allure.description_html("""<h4>This test is to verify that the contract is being send when umr is repeated</h4>""")
def test_repeated_umr_and_lcr():
    try:
        data_time = Utilidades.set_current_data_time()
        umr_code = "UMRAlreadyExists"
        lcr_code =  "LCRAlreadyExists"
        r = send_valid_json("RepeatedUmrAndLcrTemplate.json",data_time, "TestSiete",umr_code,lcr_code)
        assert r.status_code == 200
        assert r.reason == "OK"
        assert "RepeatedUmrAndLcrTemplate.json was successfully uploaded" in r.text
    except Exception as ex:
        pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)
=======
# @allure.title("Repeated umr")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when umr is repeated</h4>""")
# def test_repeated_umr_and_lcr():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = "UMRAlreadyExists"
#         lcr_code =  "LCRAlreadyExists"
#         r = send_valid_json("RepeatedUmrAndLcrTemplate.json",data_time, "TestSiete",umr_code,lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "RepeatedUmrAndLcrTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)
>>>>>>> 4a20f202f433e71e59b06e8b54ff63114e76999a

# @allure.title("ContractStatusName equal to active & contractTypeName equal to Binding Authority Agreement")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when ContractStatusName is equal to Active and ContractTypeName is equal to Binding Authority Agreement</h4>""")
# def test_contract_status_name_and_contract_type_name():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("ContractStatusNameAndContractTypeNameTemplate.json", data_time, "TestOcho", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractStatusNameAndContractTypeNameTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("ContractTypeName equal to Twin Contract & missing TestMigratedFlag")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when ContracTypeName is equal to twin contract & TestMigratedFlag is mising</h4>""")
# def test_contract_type_name_and_migrated_flag_missing():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("ContractTypeNameAndMigratedFlagMissingTemplate.json",data_time, "TestNueve", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractTypeNameAndMigratedFlagMissingTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("ContractTypeName is equal to Service Company Agreement & migratedFlag is False")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when ContracTypeName is equal to Service Company Agreement and MigratedFlag is False</h4>""")
# def test_contract_type_name_and_migrated_flag_false():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("ContractTypeNameAndMigratedFlagFalseTemplate.json",data_time, "TestDiez", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractTypeNameAndMigratedFlagFalseTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("MigratedFlag True & IsMigratedDraft False")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when MigratedFlag is True and IsMigratedDraft False</h4>""")
# def test_migrated_flag_true_and_is_migrated_draft_false():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json",data_time, "TestOnce", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "MigratedFlagTrueAndIsMigratedDraftFalseTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

@allure.title("Umr is repeated and it has preveious error")
@allure.description_html("""<h4>This test is to verify that the contract is being send when it has an umr that is repeated and it previously had an error</h4>""")
def test_umr_repeated_with_existingError():
    try:
        data_time = Utilidades.set_current_data_time()
        umr_code = "TestDoceAlreadyExistingErrors"
        lcr_code = Utilidades.create_source_system_reference_code()
        r = send_valid_json("UmrRepeatedWithExistingErrorTemplate.json", data_time, "", umr_code, lcr_code)
        assert r.status_code == 200
        assert r.reason == "OK"
        assert "UmrRepeatedWithExistingErrorTemplate.json was successfully uploaded" in r.text
    except Exception as ex:
        pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("Invalid currency")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when currency is invalid</h4>""")
# def test_invalid_currency():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("InvalidCurrencyTemplate.json", data_time, "TestTrece", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "InvalidCurrencyTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("Contract without contract currency")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when it does not have contract currency</h4>""")
# def test_contract_without_contract_currency():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("ContractWithoutContractCurrencyTemplate.json",data_time, "TestQuince", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractWithoutContractCurrencyTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("ContractStatusName is equal to Registered")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when ContractStatusName is equal to registered</h4>""")
# def test_contract_status_name_equal_registered():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("ContractStatusNameEqualRegisteredTemplate.json",data_time, "TestDieciseis", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractStatusNameEqualRegisteredTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)


# @allure.title("MigratedFlag True & IsMigratedDraft True")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when both MigratedFlag and IsMigratedFlag are True</h4>""")
# def test_migrated_flag_true_and_is_migrated_draft_true():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json",data_time, "TestDiecisiete", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "MigratedFlagTrueAndIsMigratedDraftTrueTemplate.json was successfully uploaded" in r.text    
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

# @allure.title("Contrat without ContractStatus")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when it does not have ContractStatus</h4>""")
# def test_contract_without_contract_status():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code = Utilidades.create_umr_code()
#         lcr_code =  Utilidades.create_source_system_reference_code()
#         r = send_valid_json("ContractWithoutContractStatusTemplate.json",data_time, "TestDieciocho", umr_code, lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractWithoutContractStatusTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)

<<<<<<< HEAD
@allure.title("Umr & lcr are equal")
@allure.description_html("""<h4>This test is to verify that the contract is being send when umr and lcr are equal</h4>""")
def test_contract_with_same_umr_and_lcr():
    try:
        data_time = Utilidades.set_current_data_time()
        umr_code_and_lcr_code = Utilidades.create_umr_code()
        r = send_valid_json("ContractWithSameUmrAndLcrTemplate.json",data_time, "TestDiecinueve", umr_code_and_lcr_code, umr_code_and_lcr_code)
        assert r.status_code == 200
        assert r.reason == "OK"
        assert "ContractWithSameUmrAndLcrTemplate.json was successfully uploaded" in r.text
    except Exception as ex:
        pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)
=======
# @allure.title("Umr & lcr are equal")
# @allure.description_html("""<h4>This test is to verify that the contract is being send when umr and lcr are equal</h4>""")
# def test_contract_with_same_umr_and_lcr():
#     try:
#         data_time = Utilidades.set_current_data_time()
#         umr_code_and_lcr_code = Utilidades.create_umr_code()
#         data_time = Utilidades.set_current_data_time()
#         r = send_valid_json("ContractWithSameUmrAndLcrTemplate.json",data_time, "TestDiecinueve", umr_code_and_lcr_code, umr_code_and_lcr_code)
#         assert r.status_code == 200
#         assert r.reason == "OK"
#         assert "ContractWithSameUmrAndLcrTemplate.json was successfully uploaded" in r.text
#     except Exception as ex:
#         pytest.fail(f"status: {r.status_code} \n reason: {r.reason} \n message: {r.text}", False)
>>>>>>> 4a20f202f433e71e59b06e8b54ff63114e76999a



def send_valid_json(file, data_time, id, umr_code,  lcr_code):
            t = open("./Data/SendJson/Templates/" + Configuration.set_envirnment() + "/"+ file)
            data_template = json.load(t)
            data_template['LloydsContractRef'] = id + lcr_code
            data_template['UMR'] = id + umr_code
            data_template['VersionUpdatedDate'] = data_time
            data = json.dumps(data_template)
            writable_file = open("./Data/SendJson/Templates/" + Configuration.set_envirnment() + "/" + file,'w')
            writable_file.write(data)
            writable_file.close()
            t.close()
            url = Configuration.set_url_for_json(Configuration.set_envirnment())
            headers = Configuration.set_header_for_json(Configuration.set_envirnment())
            r =  requests.post(url, files={'file': open("./Data/SendJson/Templates/" + Configuration.set_envirnment() + "/" + file, 'rb')},headers=headers) 
            return r

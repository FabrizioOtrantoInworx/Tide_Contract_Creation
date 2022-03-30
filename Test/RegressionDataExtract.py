import pyodbc
import pytest
import json
import xlrd

server = 'ltdshd01sql01.database.windows.net'
database = 'TideDWH-DEV'
username = '{DV.Fabrizio.Otranto@charlestaylor.com}'
password = '{ssssss}'
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';DATABASE='+database+';UID='+username+';PWD='+ password+'; Authentication=ActiveDirectoryInteractive') as conn:
    with conn.cursor() as cursorr:
        global cursor
        cursor = cursorr

# def test_regression_section_primary_risk_code_underwriting_reference():
#     try:
#         t = open("./Data/DataExtract/section_primary_risk_code_underwritting_reference_regression.json")
#         dataTemplate = json.load (t)
#         t.close()
#         cursor.execute("""
#         exec as user ='TideDWH_User_BRIT_TEST_DataExtract' 
#         EXEC [DataExtract].[Contract_v002_007] 
#         '2022-02-23 01:00:00.000','2022-02-24 00:00:00.000',null,null
#         """)
#         row = cursor.fetchone()
#         array_resultado = []
#         while row:
#             if row.Tide_ContractId == dataTemplate['contract_id']:
#                 valores = row.Tide_ContractId, row.Section_Primary_Risk_Code_Underwriting_Reference, row.DWH_DivisionName
#                 if len(valores) > 0: 
#                     array_resultado.append(valores)
#             row = cursor.fetchone()  
                
#         assert array_resultado[0][1] == dataTemplate["first_result"]
#         assert array_resultado[0][1] == dataTemplate["second_result"]
#         print(array_resultado)
#     except Exception as ex:
#         pytest.fail(f"Test have failed. \n\n {ex}", False)



#Regression 2.7

@pytest.mark.regression_column_name_002_007
def test_Core_Contract_column_name_002_007():
    regression_data_extract_schema("Core.Contract", "DataExtract.Contract_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_core_bordereau_column_name_002_007():
    regression_data_extract_schema("Core.Bordereau", "DataExtract.Bordereau_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_core_bordereau_financial_column_name_002_007():
    regression_data_extract_schema("Core.Bordereau_Financial", "DataExtract.Bordereau_Financial_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_transactional_claim_expert_column_name_002_007():
    regression_data_extract_schema("Transactional.Claim_Expert", "DataExtract.Claim_Expert_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_transactional_claim_column_name_002_007():
    regression_data_extract_schema("Transactional.Claim", "DataExtract.Claim_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_core_contract_claims_authority_column_name_002_007():
    regression_data_extract_schema("Core.Contract_ClaimsAuthority", "DataExtract.Contract_ClaimsAuthority_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_core_contract_market_column_name_002_007():
    regression_data_extract_schema("Core.Contract_Market", "DataExtract.Contract_Market_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_core_contract_reportging_channel_column_name_002_007():
    regression_data_extract_schema("Core.Contract_ReportingChannel", "DataExtract.Contract_ReportingChannel_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_core_contract_risk_codes_column_name_002_007():
    regression_data_extract_schema("Core.Contract_Risk_Codes", "DataExtract.Contract_Risk_Codes_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_core_contract_rule_breach_column_name_002_007():
    regression_data_extract_schema("Core.Contract_Rule_Breach", "DataExtract.Contract_Rule_Breach_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_core_contract_section_location_column_name_002_007():
    regression_data_extract_schema("Core.Contract_Section_Location", "DataExtract.Contract_Section_Location_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_core_contract_version_column_name_002_007():
    regression_data_extract_schema("Core.Contract_Version", "DataExtract.Contract_Version_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_transactional_premium_tax_column_name_002_007():
    regression_data_extract_schema("Transactional.Premium_Tax", "DataExtract.Premium_Tax_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_transactional_premium_column_name_002_007():
    regression_data_extract_schema("Transactional.Premium", "DataExtract.Premium_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_transactional_risk_coverage_column_name_002_007():
    regression_data_extract_schema("Transactional.Risk_Coverage", "DataExtract.Risk_Coverage_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_transactional_risk_tax_column_name_002_007():
    regression_data_extract_schema("Transactional.Risk_Tax", "DataExtract.Risk_Tax_v002_007", "2.7")

@pytest.mark.regression_column_name_002_007
def test_transactional_risk_column_name_002_007():
    regression_data_extract_schema("Transactional.Risk", "DataExtract.Risk_v002_007", "2.7")


#Regresion 2.6
@pytest.mark.regression_column_name_002_006
def test_Core_Contract_column_name_002_006():
    regression_data_extract_schema("Core.Contract", "DataExtract.Contract_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_core_bordereau_column_name_002_006():
    regression_data_extract_schema("Core.Bordereau", "DataExtract.Bordereau_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_core_bordereau_financial_column_name_002_006():
    regression_data_extract_schema("Core.Bordereau_Financial", "DataExtract.Bordereau_Financial_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_transactional_claim_expert_column_name_002_006():
    regression_data_extract_schema("Transactional.Claim_Expert", "DataExtract.Claim_Expert_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_transactional_claim_column_name_002_006():
    regression_data_extract_schema("Transactional.Claim", "DataExtract.Claim_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_core_contract_claims_authority_column_name_002_006():
    regression_data_extract_schema("Core.Contract_ClaimsAuthority", "DataExtract.Contract_ClaimsAuthority_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_core_contract_market_column_name_002_006():
    regression_data_extract_schema("Core.Contract_Market", "DataExtract.Contract_Market_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_core_contract_reportging_channel_column_name_002_006():
    regression_data_extract_schema("Core.Contract_ReportingChannel", "DataExtract.Contract_ReportingChannel_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_core_contract_risk_codes_column_name_002_006():
    regression_data_extract_schema("Core.Contract_Risk_Codes", "DataExtract.Contract_Risk_Codes_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_core_contract_rule_breach_column_name_002_006():
    regression_data_extract_schema("Core.Contract_Rule_Breach", "DataExtract.Contract_Rule_Breach_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_core_contract_section_location_column_name_002_006():
    regression_data_extract_schema("Core.Contract_Section_Location", "DataExtract.Contract_Section_Location_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_core_contract_version_column_name_002_006():
    regression_data_extract_schema("Core.Contract_Version", "DataExtract.Contract_Version_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_transactional_premium_tax_column_name_002_006():
    regression_data_extract_schema("Transactional.Premium_Tax", "DataExtract.Premium_Tax_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_transactional_premium_column_name_002_006():
    regression_data_extract_schema("Transactional.Premium", "DataExtract.Premium_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_transactional_risk_coverage_column_name_002_006():
    regression_data_extract_schema("Transactional.Risk_Coverage", "DataExtract.Risk_Coverage_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_transactional_risk_tax_column_name_002_006():
    regression_data_extract_schema("Transactional.Risk_Tax", "DataExtract.Risk_Tax_v002_006", "2.6")

@pytest.mark.regression_column_name_002_006
def test_transactional_risk_column_name_002_006():
    regression_data_extract_schema("Transactional.Risk", "DataExtract.Risk_v002_006", "2.6")


#Regression 2.5

@pytest.mark.regression_column_name_002_005
def test_Core_Contract_column_name_002_005():
    regression_data_extract_schema("Core.Contract", "DataExtract.Contract_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_core_bordereau_column_name_002_005():
    regression_data_extract_schema("Core.Bordereau", "DataExtract.Bordereau_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_core_bordereau_financial_column_name_002_005():
    regression_data_extract_schema("Core.Bordereau_Financial", "DataExtract.Bordereau_Financial_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_transactional_claim_expert_column_name_002_005():
    regression_data_extract_schema("Transactional.Claim_Expert", "DataExtract.Claim_Expert_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_transactional_claim_column_name_002_005():
    regression_data_extract_schema("Transactional.Claim", "DataExtract.Claim_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_core_contract_claims_authority_column_name_002_005():
    regression_data_extract_schema("Core.Contract_ClaimsAuthority", "DataExtract.Contract_ClaimsAuthority_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_core_contract_market_column_name_002_005():
    regression_data_extract_schema("Core.Contract_Market", "DataExtract.Contract_Market_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_core_contract_reportging_channel_column_name_002_005():
    regression_data_extract_schema("Core.Contract_ReportingChannel", "DataExtract.Contract_ReportingChannel_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_core_contract_rule_breach_column_name_002_005():
    regression_data_extract_schema("Core.Contract_Rule_Breach", "DataExtract.Contract_Rule_Breach_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_core_contract_version_column_name_002_005():
    regression_data_extract_schema("Core.Contract_Version", "DataExtract.Contract_Version_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_transactional_premium_tax_column_name_002_005():
    regression_data_extract_schema("Transactional.Premium_Tax", "DataExtract.Premium_Tax_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_transactional_premium_column_name_002_005():
    regression_data_extract_schema("Transactional.Premium", "DataExtract.Premium_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_transactional_risk_coverage_column_name_002_005():
    regression_data_extract_schema("Transactional.Risk_Coverage", "DataExtract.Risk_Coverage_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_transactional_risk_tax_column_name_002_005():
    regression_data_extract_schema("Transactional.Risk_Tax", "DataExtract.Risk_Tax_v002_005", "2.5")

@pytest.mark.regression_column_name_002_005
def test_transactional_risk_column_name_002_005():
    regression_data_extract_schema("Transactional.Risk", "DataExtract.Risk_v002_005", "2.5")


def regression_data_extract_schema(sheet, schema_name, schema_version):
    try:
        book = xlrd.open_workbook(f"./Data/DataExtract/DataSchema{schema_version}.xls")
        worksheet = book.sheet_by_name(sheet)
        sheet_row = 1
        cursor.execute(f"""
            exec as user ='TideDWH_User_BRIT_TEST_DataExtract'
            EXEC [DataExtract].[DataExtractSchema] 
            @DataExtract_Name = '{schema_name}', 
            @ResultId = null, @Result_Narrative = null
            """)
        row = cursor.fetchone()
        array_resultado = []
        while row:
                valores = row.Column_Name
                if len(valores) > 0: 
                    array_resultado.append(valores)
                row = cursor.fetchone()  
                
        for column_name in array_resultado:
             assert column_name == worksheet.cell(sheet_row,0).value
             print(f"{column_name} == {worksheet.cell(sheet_row,0).value}")
             sheet_row +=1
    except Exception as ex:
        pytest.fail(f"Test have failed. \n\n {ex}", False)
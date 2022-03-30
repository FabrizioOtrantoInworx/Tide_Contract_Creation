import pyodbc
server = 'ltdshd01sql01.database.windows.net'
database = 'TideDWH-DEV'
username = '{DV.Fabrizio.Otranto@charlestaylor.com}'
password = '{b9zQ=PV2}'   
driver= '{ODBC Driver 17 for SQL Server}'

with pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';DATABASE='+database+';UID='+username+';PWD='+ password+'; Authentication=ActiveDirectoryInteractive') as conn:
    with conn.cursor() as cursor:
        cursor.execute("exec as user ='TideDWH_User_BRIT_TEST_DataExtract' EXEC [DataExtract].[Contract_v002_007] '2022-02-21 01:00:00.000','2022-02-22 00:00:00.000',null,null")
        row = cursor.fetchone()
        while row:
                print (str(row[0]) + " " + str(row[3]))
                row = cursor.fetchone()

import json
from outscraper import ApiClient

import openpyxl
 
doc = openpyxl.load_workbook ("webs.xlsx")
hoja = doc.get_sheet_by_name("webs")
 
webs=[]
for row in hoja.iter_rows(min_row=2):
    pages = row[0].value
    webs.append(pages)

api_client = ApiClient(api_key='Z29vZ2xlLW9hdXRoMnwxMTE0OTA0MzI1MDM2NTczMTMwODl8NDc3MzA4N2MxNw')

# short_list = [
# ] 

# Search for businesses in specific locations:
result = api_client.emails_and_contacts(webs)

with open('./json_files/mexexterior.json', 'w') as file:
    json.dump(result, file, indent=4)
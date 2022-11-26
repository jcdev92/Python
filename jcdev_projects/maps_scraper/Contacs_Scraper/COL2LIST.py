import openpyxl
 
doc = openpyxl.load_workbook ("webs.xlsx")
hoja = doc.get_sheet_by_name("webs")
 
webs=[]
for row in hoja.iter_rows(min_row=2):
    pages = row[0].value
    webs.append(pages)

print(webs)
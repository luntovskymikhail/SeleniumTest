import openpyxl

#set path, open file, specify the sheet
path = "C://Users//Mikhail//PycharmProjects//SeleniumTest//Book1.xlsx"
wb = openpyxl.load_workbook(path)
sheet = wb["List2"]

for r in range (1, 4):
    for c in range(1, 3):
        sheet.cell(row=r, column=c).value="Test"

wb.save(path)

'''
Result:
Test	Test
Test	Test
Test	Test
'''
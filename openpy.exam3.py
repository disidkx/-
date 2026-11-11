from openpyxl import *
from openpyxl.styles import PatternFill

wb= Workbook()
ws= wb.active

ws['A1'] = '이름'
ws['B1'] = '국어'
ws['C1'] = '수학'

color = PatternFill(fill_type='solid' , fgColor='FFFF00')


for cell in ws[1]:
    cell.fill=color

wb.save('openpyxl/bg_color.xlsx')

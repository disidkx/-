from openpyxl import *

w2 = load_workbook('test.xlsx')

new_ws = w2.create_sheet()

new_ws.title= '마지막_시트'

w2 = load_workbook('openpyxl/test.xlsx')

new_ws = w2.create_sheet()


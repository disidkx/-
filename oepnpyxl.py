

#oprnpyxl 불러오기/모든 기능을 불러옴
import openpyxl 

# from openpyxl import *

#버전확인
print(openpyxl.__version__)




from openpyxl import Workbook

w1 = Workbook()
ws = w1.active
w1.save('test.xlsx')


w2 = load_workbook('test.xlsx')

ws2 = w2.active

ws2['A1'] = 'hello'

w2.save('text.xlsx')



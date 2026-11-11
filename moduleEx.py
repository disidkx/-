

import time
#프로그램을 3초동안 멈춤
time.sleep(3)
#3초가 지난 후 출력
print("3초 후 실행")

#시스템 모듈
#파이썬 실행 환경을 다루는 모듈
import sys

#현재 사용중인 파이썬 버전 출력
print(sys.version)

#운영체제와 관련된 기능 제공
#파일/폴더 경로 처리에 사용
import os
#현재 작업중인 폴더경로 출력
print(os.getcwd())

#데이터 형식 모듈
#json형식으로 데이터를 변환
#JSON : 데이터를 약속된 모양으로 적는 방식("key:valu" 딕셔너리 형식이랑 같음)
# 웹, API 저장에 사용
#API : 프로그램끼리 대화하는 방법(규칙)

import json
date = {
    'name' :'jin',
    'age' : 22
}
print(json.dumps(date))

#정규 표현식 모듈
#문자열 패턴 검사 모듈
#형식 확인 (아이디, 이메일)에 사용

import re

#문자열이 hi로 시작하는지 확인
print(bool(re.match('hi','hi python')))

#csv 파일 모듈
#csv(엑셀) 파일을 읽고 쓰는 모듈
# 데이터 저장/분석 기초에 사용

import csv 
with open('test.scv','w',newline='') as f:
    csv.writer(f).writerow(['name','score'])

#자료구조 모듈 
#자료구조를 편하게 쓰도록 도와줌
#카운트, 큐 ,딕셔너리 확장 기능 제공

from collections import Counter

#문자열에서 각 글자의 개수를 셈
print (Counter('apple'))


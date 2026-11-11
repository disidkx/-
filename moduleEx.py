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

from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

import time
from urllib import request

# 실행경로와 드라이버 객체 생성

inp = int(input("가져올 개수를 입력하세요 : "))
l = []
driver = webdriver.Chrome()

wb = load_workbook('study.xlsx',
                   read_only=False,  # 읽기 전용(읽기 전용에 최적화되어 파일을 불러온다)
                   # False면 셀안 공식을 가져오고 True면 공식 적용된 값만을 불러온다.
                   data_only=False,
                   )
sheet1 = wb['Sheet1']  # Sheet1 시트를 가져오기.
sheet1['G1'].value = "발음"
for i in range(2,inp+2):
    l.append(sheet1[f'B{i}'].value)
    print(l)
for i in range(len(l)):
    print(l[i])
    d = i+2
    time.sleep(2)
    driver.get(f"https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query={l[i]}")
    time.sleep(1)
    try :
        elem = driver.find_element(By.CLASS_NAME,"key").text
    except :
        elem = ""
    sheet1[f'G{d}'].value = elem
driver.close()
wb.save(filename='study.xlsx') #파일 study.xlsx로 덮어쓰기.
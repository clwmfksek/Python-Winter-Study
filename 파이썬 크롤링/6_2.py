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
driver.get("https://www.op.gg/summoners/kr/%EC%B9%98%20%EC%A6%88-%EC%B9%98%20%EC%A6%88")

wb = load_workbook('opgg.xlsx',
                   read_only=False,  # 읽기 전용(읽기 전용에 최적화되어 파일을 불러온다)
                   # False면 셀안 공식을 가져오고 True면 공식 적용된 값만을 불러온다.
                   data_only=False,
                   )
sheet1 = wb['Sheet']  # Sheet1 시트를 가져오기.
sheet1['A1'] = "게임 종류"
sheet1['B1'] = "킬"
sheet1['C1'] = "데스"
sheet1['D1'] = "어시"
sheet1['E1'] = "등수"

for i in range(2,inp+2):
    try :
        sheet1[f"A{i}"].value = driver.find_element(By.XPATH,
                                                    f'//*[@id="content-container"]/div[2]/div[3]/div[{i-1}]/div/div[2]/div/div[1]/div[1]/div[1]').text
        sheet1[f"B{i}"].value = driver.find_element(By.XPATH,
                                                    f'//*[@id="content-container"]/div[2]/div[3]/div[{i}]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span[1]').text
        sheet1[f"C{i}"].value = driver.find_element(By.XPATH,
                                                    f'//*[@id="content-container"]/div[2]/div[3]/div[{i}]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span[2]').text
        sheet1[f"D{i}"].value = driver.find_element(By.XPATH,
                                                    f'//*[@id="content-container"]/div[2]/div[3]/div[{i}]/div/div[2]/div/div[2]/div[1]/div[2]/div[1]/span[3]').text
        try :
            sheet1[f"E{i}"].value = driver.find_element(By.XPATH,
                                                        f'//*[@id="content-container"]/div[2]/div[3]/div[{i}]/div/div[2]/div/div[2]/div[2]/div/div/button/div/div').text
        except :
            sheet1[f"E{i}"].value = ""
    except :
        driver.find_element(By.XPATH,'//*[@id="content-container"]/div[2]/button').click()

driver.close()
wb.save(filename='opgg.xlsx') #파일 study.xlsx로 덮어쓰기.
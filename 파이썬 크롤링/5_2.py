# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib import request

# 실행경로와 드라이버 객체 생성

inp = input("검색할 단어를 입력하세요 : ")
l = int(input("뽑아올 개수를 입력하세요 : "))
driver = webdriver.Chrome()
driver.get(f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={inp}")

for i in range(1,l+1):
    try :
        el = driver.find_element(By.XPATH,f'//*[@id="main_pack"]/section[2]/div[1]/div/div/div[1]/div[{i}]/div/div/div/img')
        el_url = el.get_attribute('src')
        request.urlretrieve(el_url, f"./photo/{inp}_{i}.jpg")
    except :
        element = driver.find_element(By.XPATH,'//*[@id="footer"]')
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight);", element)]
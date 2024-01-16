# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from urllib import request

# 실행경로와 드라이버 객체 생성

num = 0
driver = webdriver.Chrome()
driver.get(f"https://cafe.naver.com/joonggonara/994948311")
time.sleep(3)
driver.switch_to.frame('cafe_main')
imgs = driver.find_elements(By.TAG_NAME,"img")
for img in imgs:
    el_url = img.get_attribute('src') 
    print(el_url)
    request.urlretrieve(el_url, f"./img/{num}.jpg")
    num += 1
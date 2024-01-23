from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
# 예: 10초 동안 기다리며 특정 요소가 나타날 때까지 대기
driver = webdriver.Chrome()
driver.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EC%A7%80%EC%88%98")
try :
    driver.find_element(By.ID,'main_packkkkk')
except NoSuchElementException as e:
    print("요소를 찾을 수 없습니다.")
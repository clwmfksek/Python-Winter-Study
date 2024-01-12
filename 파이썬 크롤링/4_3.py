from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome()

url = "https://cafe.naver.com/joonggonara/994948311"
driver.get(url)

time.sleep(3)
driver.switch_to.frame('cafe_main')
element = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]').text
print(element)
for i in driver.find_elements(By.CSS_SELECTOR,'img'): # img 태그를 가져옴
    print(i.get_attribute("src")) # img 태그의 src 속성을 가져옴
time.sleep(3)
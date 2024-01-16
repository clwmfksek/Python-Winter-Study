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
driver.switch_to.frame('cafe_main')
time.sleep(3)
element = driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[1]/div[1]/div/h3')
driver.execute_script("")
driver.execute_script("let dt = new Date(); arguments[0].innerText = `${dt.getFullYear()}년 ${dt.getMonth()+1}월 ${dt.getDate()}일`;", element)
time.sleep(25)
driver.quit()
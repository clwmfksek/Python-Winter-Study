from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup
import re

driver = webdriver.Chrome()

url = "http://capszzang.gq/"
driver.get(url)

time.sleep(3)
element = driver.find_element(By.XPATH,'//*[@id="footer"]/div/div[2]/div')
driver.execute_script("arguments[0].innerText = '반갑습니다';", element)

time.sleep(3)
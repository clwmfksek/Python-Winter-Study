# 라이브러리 불러옴
from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from urllib import request

# 실행경로와 드라이버 객체 생성

driver = webdriver.Chrome()
driver.maximize_window()
driver.fullscreen_window()
time.sleep(3)
driver.get("https://everytime.kr/")
driver.fullscreen_window()
time.sleep(2)
driver.switch_to.new_window('tab')
driver.get("https://mdrims.dongguk.edu/")
time.sleep(3)
driver.switch_to.window(driver.window_handles[0])
driver.fullscreen_window()
time.sleep(3)
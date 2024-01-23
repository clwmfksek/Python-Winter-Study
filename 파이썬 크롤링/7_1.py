from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# 예: 10초 동안 기다리며 특정 요소가 나타날 때까지 대기
driver = webdriver.Chrome()
driver.get("http://naver.com")
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'query'))
)

driver.find_element(By.XPATH,'//*[@id="query"]').send_keys('지수')
driver.implicitly_wait(5)

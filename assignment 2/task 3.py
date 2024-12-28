import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('http://www.automationpractice.pl/index.php')
time.sleep(1)
driver.find_element(By.CLASS_NAME,'login').click()
time.sleep(1)

driver.quit()

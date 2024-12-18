"search on google by name attribute"

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.google.com/')
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("python programming language")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"gNO89b").click()
time.sleep(2)
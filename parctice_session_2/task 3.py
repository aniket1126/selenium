"selenium website to open projects"

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.selenium.dev/')
link=driver.find_elements(By.CLASS_NAME,"nav-item")
link[3].click()
time.sleep(2)
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://demo.guru99.com/test/newtours/")
driver.find_element(By.XPATH,"//*[@href='register.php']").click()
time.sleep(2)
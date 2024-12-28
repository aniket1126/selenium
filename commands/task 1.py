import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.w3schools.com/html/html_forms.asp")
button=driver.find_element(By.XPATH,"//*[@id='main']/div[3]/div/form/input[3]")
print(button.is_enabled())

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.w3schools.com/html/html_forms.asp")
bike=driver.find_element(By.XPATH,"//*[@id='vehicle1']")
bike.click()
car=driver.find_element(By.XPATH,"//*[@id='vehicle2']")
car.click()

print(bike.is_selected())
print(car.is_selected())
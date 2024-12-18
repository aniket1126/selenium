import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get('https://www.wikipedia.org/')
driver.find_element(By.XPATH,"/html/body/main/div/form/fieldset/div/input").send_keys("tesing api")
time.sleep(2)
driver.find_element(By.TAG_NAME,"button").click()
time.sleep(2)
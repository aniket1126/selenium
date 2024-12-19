import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

"login script for demo.guru99"
driver.get('https://www.demo.guru99.com/test/newtours/')
driver.find_element(By.NAME,"userName").send_keys("Aniket123")
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("aniket@123")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[2]/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form/table/tbody/tr[4]/td/table/tbody/tr[4]/td[2]/div/input").click()
time.sleep(2)

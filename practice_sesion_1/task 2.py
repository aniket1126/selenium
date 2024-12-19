import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(2)
driver.find_element(By.CLASS_NAME,"oxd-input").send_keys("Admin")
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()
time.sleep(2)
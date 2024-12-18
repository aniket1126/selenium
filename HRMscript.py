import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from googlescript import driver

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(3)

username_field = driver.find_element(By.NAME, "username")
password_field = driver.find_element(By.NAME, "password")

username_field.send_keys("Admin")
time.sleep(2)
password_field.send_keys("admin123")
time.sleep(2)
login_button = driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
time.sleep(5)


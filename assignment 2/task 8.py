import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.facebook.com")

facebook_button = driver.find_element(By.XPATH, "//a[@title='Facebook']").click()

time.sleep(5)

driver.quit()

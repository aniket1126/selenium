"task 5 web driver opens"
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.selenium.dev/documentation/')
driver.find_element(By.PARTIAL_LINK_TEXT,"WebDriver").click()
time.sleep(2)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.python.org/")
expected_url="https://www.python.org/"
actual = driver.current_url
if actual == expected_url:
    print("the url is matched ")
else:
    print("not mathced")

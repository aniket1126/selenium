import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.python.org/")
keyword="Python.org"
actual = driver.title
if keyword in actual:
    print("reached to site")
else: print("not reched")

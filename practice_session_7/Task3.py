import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select


serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# drpdwn = Select(driver.find_element(By.XPATH,"//*[@id='country']"))


# Task 1 - Select By VisibleText
# drpdwn.select_by_visible_text("India")
# time.sleep(2)

# Task 2 - Select By Index
# drpdwn.select_by_index(3)
# time.sleep(3)

# Task 3
# drpdwn = driver.find_elements(By.XPATH,"//*[@id='country']")
# for i in drpdwn:
#     print(i.text)


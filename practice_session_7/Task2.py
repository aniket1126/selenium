
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.devtools.v129.fed_cm import click_dialog_button
from selenium.webdriver.support.select import Select

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Task 1
# all = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
# time.sleep(2)
# for i in range(len(all)):
#     all[i].click()
# time.sleep(2)

# Task 2
# driver.find_element(By.ID,"tuesday").click()
# time.sleep(2)

# Task 3
# all = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
# time.sleep(2)
# for i in range(len(all)):
#     all[i].click()
# time.sleep(2)
#
# for i in all:
#     if i.is_selected():
#         i.click()
# time.sleep(2)
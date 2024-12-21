"locate email with the help of password with above"
from pydoc import locate

from selenium.webdriver.support.relative_locator import locate_with

# emial locator=locate_with(By.tagname,"input").above({By.id:"password"})

"types of relative locators"
# near
# above and below
# to_left_of and to_right_of
# with tagname
# near and with tagname

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service
# driver.maximize_window()

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

"left of the book"
# driver.get("https://automationbookstore.dev/")
# left =driver.find_element(locate_with(By.TAG_NAME,"li").to_left_of({By.ID:"pid2"})).text
# print(left)

"right of the book"
# driver.get("https://automationbookstore.dev/")
# right =driver.find_element(locate_with(By.TAG_NAME,"li").to_right_of({By.ID:"pid2"})).text
# print(right)

"below"
# driver.get("https://automationbookstore.dev/")
# below =driver.find_element(locate_with(By.TAG_NAME,"h2").below({By.ID:"pid2_title"})).text
# print(below)

"above"
driver.get("https://automationbookstore.dev/")
above=driver.find_element(locate_with(By.TAG_NAME,"h2").above({By.ID:"pid6_title"})).text
print(above)



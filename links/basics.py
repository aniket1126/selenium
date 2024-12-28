# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import  Service
# from urllib3 import request
#
# service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)
#
# driver.get('http://www.deadlinkcity.com/')
# all=driver.find_elements(By.TAG_NAME,"a")
# time.sleep(2)
# print(len(all))
#
# for link in all:
#     url = link.get_attribute('href')
#     try:
#         request.head(url)
#         print(url,"is broken link")
#         count+=1
#

import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('http://www.deadlinkcity.com/')

all_links = driver.find_elements(By.TAG_NAME, "a")
time.sleep(2)
count = 0

print(f"Total number of links found: {len(all_links)}")

# for link in all_links:
#     url = link.get_attribute('href')
#     try:
#             response = requests.head(url)
#     except:
#             None
#     if response.status_code >= 400:
#         count += 1
#         print(count)
#     except requests.RequestException as e:
#             print(f"Error accessing {url}: {e}")
#
# print(f"Total broken links found: {count}")

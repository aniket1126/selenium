import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

"child"
driver.get("https://money.rediff.com/gainers")
# child = driver.find_elements(By.XPATH,"//td[text()='62.72']/parent::tr/child::td")
# print(len(child))

"following"
# following = driver.find_elements(By.XPATH, "//td[text()='62.72']/parent::tr/following::tr")
# print(len(following))

"following sibling"
# following = driver.find_elements(By.XPATH, "//td[text()='62.72']/following-sibling::td")
# print(len(following))

"parent"
# parent = driver.find_elements(By.XPATH, "//td[text()='62.72']/parent::tr")
# print(len(parent))

"preceding"
# preceding = driver.find_elements(By.XPATH, "//td[text()='62.72']/parent::tr/preceding::tr")
# print(len(preceding))


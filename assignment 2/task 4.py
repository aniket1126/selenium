from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://en.wikipedia.org/wiki/Website')

h1_element = driver.find_element(By.TAG_NAME, 'h1').text
print(h1_element)

driver.quit()

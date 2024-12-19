import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get('https://www.facebook.com/login/')

"Xpath with and"
# driver.find_element(By.XPATH,"//input[@name='email' and @id='email']").send_keys("123")
# time.sleep(2)


"Xpath with or"
# driver.find_element(By.XPATH,"//input[@name='aniket' or @id='pass']").send_keys("123")
# time.sleep(2)

"Xpath with contains"
# driver.find_element(By.XPATH,"//*[contains(@placeholder,'Email address or phone number')]").send_keys("!23")
# time.sleep(2)

"Xpath with start"
# driver.find_element(By.XPATH,"//input[starts-with(@id,'em')]").send_keys("aniket")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[starts-with(@id,'pa')]").send_keys("aniket123")
# time.sleep(2)

"Xpath ends with"
# driver.find_element(By.XPATH,"//input[ends-with(@id,'il')]").send_keys("aniket")
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[ends-with(@id,'ss')]").send_keys("aniket123")
# time.sleep(2)


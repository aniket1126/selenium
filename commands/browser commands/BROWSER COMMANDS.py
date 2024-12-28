"browser commands"
# driver.close() -- close the current window where driver instance is points
# driver.quit()  -- close all the windows that are opening

"EXAMPLE"
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

"USE OF CLOSE AND QUIT COMMANDS"
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.close()
time.sleep(3)
driver.quit()

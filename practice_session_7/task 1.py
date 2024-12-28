
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Implicitly Wait
# driver.implicitly_wait(10)
# username = driver.find_element(By.NAME,"username")
# username.send_keys("Admin")

# Explicit Wait
# mywait = WebDriverWait(driver,5)
# mywait.until(EC.presence_of_element_located((By.CLASS_NAME,"orangehrm-login-button"))).click()

# Fluent Wait
# mywait = WebDriverWait(driver,20,poll_frequency=2,ignored_exceptions=[NoSuchElementException])
# mywait.until(EC.presence_of_element_located((By.CLASS_NAME,"orangehrm-login-button"))).click()
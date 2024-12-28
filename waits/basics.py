"basics for waits"



from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.support.wait import WebDriverWait

"types of wait"
#implicient wait  --- wait for element   driver.implicitly.wait(2)
# explicit wait   --- first declare then use, and use a webdriver class
# fluent wait     --- extension of explicit wait

"explicit wait"
# wait=WebdriverWait(driver,2)
# link=wait.until(EC.presence_of_element_located*By.Xpath,"// [' ']")))

"fluent wait"
# wait=WebdriverWait(driver,2,poll_frequency=2,ignored_exception)
# link=wait.until(EC.presence_of_element_located*By.Xpath,"// [' ']")))


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
import wait

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# driver.implicitly_wait(5)
# driver.get("https://www.google.com/")
# Wait = WebDriverWait(driver,2)
# link= Wait.until(EC.presence_of_element_located(By.NAME,"q"))
# link.send_keys("selenium")
# search_button = wait.until(EC.element_to_be_clickable((By.NAME, "btnK")))
#
# search_button.click()
# wait.until(EC.presence_of_element_located((By.ID, "search")))
#
# print(driver.title)
# username_field = driver.find_element(By.NAME, "username")
# password_field = driver.find_element(By.NAME, "password")

# username_field.send_keys("Admin")
# driver.implicitly_wait(5)
# password_field.send_keys("admin123")
# driver.implicitly_wait(5)
# login_button = driver.find_element(By.CLASS_NAME, "orangehrm-login-button").click()
# driver.implicitly_wait(5)

driver.get("https://www.google.com/")
mywait = WebDriverWait(driver,6,poll_frequency=2,ignored_exceptions=[NoSuchElementException,ElementNotInteractableException])
search_box= mywait.until(EC.presence_of_element_located((By.NAME,"q")))
search_box.send_keys("selenium")
mywait.until(EC.element_to_be_clickable((By.NAME, "btnK"))).click()




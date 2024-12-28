# https://the-internet.herokuapp.com/javascript_alerts
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

# driver.get("https://the-internet.herokuapp.com/javascript_alerts")

"JS ALERT"
# confirm=driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button")
# confirm.click()
# time.sleep(3)
# alert=driver.switch_to.alert
# alert.accept()
# alert.dismiss()

"JS prompt"
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[3]/button").click()
# time.sleep(3)
# prompt=driver.switch_to.alert
# prompt.send_keys("aniket")
# time.sleep(2)
# prompt.accept()
# time.sleep(2)

"JS CONFIRM"
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[2]/button").click()
# time.sleep(3)
# confirm=driver.switch_to.alert
# confirm.accept()
# time.sleep(2)

"AUTHENTICATION POPUPS"
# driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
# time.sleep(2)
# expected = "Congratulations! You must have the proper credentials."
# actual = driver.find_element(By.XPATH,"//*[@id='content']/div/p").text
#
# if actual == expected:
#     print("pass")
# else:print("not proper")

"AD POPUPS"
# ops=webdriver.ChromeOptions()
# ops.add_argument("--disable-notification__")
# driver=webdriver.Chrome(ops)
# driver.get("https://whatmylocation.com/#google_vignette")
# driver.maximize_window()

"DATE PICKER"


















































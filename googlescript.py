#open the browser
#pass the url "https://www.goggle.com/"           (driver.get(""))
#capture the text box
#send values "selenium"
#valdiate

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

# from selenium.webdriver.chrome import webdriver
# from selenium.webdriver.chrome.service import service
# from selenium.webdriver.common.by import By

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
# driver = webdriver.Chrome(service=service_obj)

'APPROACH 2'
#this will open the browser
driver = webdriver.Chrome()
time.sleep(1)
#OPEN THE URL TO THE BROWSER
driver.get("https://www.google.com/")
time.sleep(1)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium")
time.sleep(1)
driver.find_element(By.NAME, "btnK").click()
time.sleep(2)

exp_title="selenium - Google Search"
result=driver.title
if exp_title == result:
    print("test pass")
else:
    print("fail")
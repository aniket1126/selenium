"naviagtional commands"
# back()
# forward()
# refresh()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# driver.get("https://www.amazon.in/?&tag=googhydrabk1-21&ref=pd_sl_1cfjttkdmt_e&adgrpid=155259812393&hvpone=&hvptwo=&hvadid=674842289452&hvpos=&hvnetw=g&hvrand=6421469239225535728&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9303358&hvtargid=kwd-28878962&hydadcr=14456_2316417&gad_source=1")
#
driver.get("https://www.flipkart.com/")
# driver.back()
# print(driver.title)
# driver.forward()
# print(driver.title)
# driver.refresh()

button=driver.find_element(By.NAME,"q")
print(button.get_attribute("title"))











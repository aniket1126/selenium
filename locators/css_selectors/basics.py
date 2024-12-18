"css selectiors"

# tag and id
# tag and class
# tag and attribute
# tag,class and attribute

"TAG AND ID"
"TAG USE #"
# driver.find_element(By.CSS_SELECTOR,"#email")

"CLASS USE /"


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

"USING TAG AND ID"
# driver.get("https://www.facebook.com/login/")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Aniket")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("@123")
# time.sleep(2)

"using tag and class"
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input._1kbt").send_keys("Aniket")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input._9npi").send_keys("@123")
# time.sleep(2)

"using tag and attribute"
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input[name=email]").send_keys("Aniket")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input[name=pass]").send_keys("@123")
# time.sleep(2)

"USING TAG CLASS AND ATTRIBUTE"
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input._1kbt[name=email]").send_keys("Aniket")
# time.sleep(2)
# driver.find_element(By.CSS_SELECTOR,"input._9npi[name=pass]").send_keys("@123")
# time.sleep(2)

"XPATH"
# xpath is xml path
# html/head/body/div/div[3]/input (absolute mode)

"2 TYPES OF X PATH"
# absolute  "/"   it uses tag name to find the element
# relative   "//"  it uses attribute name to find the element

#xpath=//tagname[@attribute="value"]
driver.get("https://online.btes.co.in/login/index.php")



driver.find_element(By.XPATH,"//input[@id='username']").send_keys("aniket@123")
time.sleep(2)

driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/section/div/div[2]/div/div/div/div/div[2]/div[1]/form/div[2]/input").send_keys("Aniket@123")

time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div/section/div/div[2]/div/div/div/div/div[2]/div[1]/form/button").click()
time.sleep(2)

driver.find_element(By.CLASS_NAME,"aalink").click()
time.sleep(2)
actual=driver.find_element(By.XPATH,"//*[@id='page-header']/div/div/div/div[1]/div[1]/div/div/h1").text
exp = 'SDET with Python-AI for IT&R'
print(actual)
if actual == exp:
    print("test pass")
else:
    print("test fail")


# actual=driver.find_element(By.XPATH,"//*[@id='action-menu-toggle-1']/span/span[1]").text
# exp = "Aniket aniket"
# if actual == exp:
#     print("test pass")
# else:
#     print("test fail")



































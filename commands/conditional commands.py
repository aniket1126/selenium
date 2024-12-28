# "conditional statement" --- "it will return true or false"

# is_display()  --- whether element is displayed or not
# is_enabled()  --- check element is enabled or not
# is_selected() --- check radio/check box is selected or not

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# logo=driver.find_element(By.CLASS_NAME,"header-logo")
# print(logo.is_enabled())
# print(logo.is_displayed())


"RADIO BUTTONS"
radiomale=driver.find_element(By.XPATH,"//*[@id='gender-male']")
radiofemale=driver.find_element(By.XPATH,"//*[@id='gender-female']")

radiomale.click()
print("the buttom is selected",radiomale.is_selected())
print("the button is selcted female",radiofemale.is_selected())

radiofemale.click()
print("the button is selcted female",radiofemale.is_selected())
print("the buttom is selected",radiomale.is_selected())




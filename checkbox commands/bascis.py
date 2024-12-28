import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

"TO SELECT ALL THE CHECKBOXES"
all = driver.find_elements(By.XPATH,"//input[@class='form-check-input' and @type='checkbox']")
time.sleep(2)
# for i in all:
#     i.click()


# for i in range(len(all)):
#     all[i].click()
#     time.sleep(2)

"TO SELECT THE SPECIFIC LAST TWO CHECKBOX"
for i in range(len(all)-2,(len(all))):
    all[i].click()

"TO UNSELECT"
for i in all:
    if i.is_selected():
        i.click()












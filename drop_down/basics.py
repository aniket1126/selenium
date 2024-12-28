# select by value
# select by index
# select by visible text
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

drop_down=Select(driver.find_element(By.XPATH,"//*[@id='country']"))
# drop_down.select_by_visible_text("India")
# time.sleep(2)

"SELECT BY INDEX"
# drop_down.select_by_index(2)

"SELECT BY VALUE"
# drop_down.select_by_value("uk")


"all options"
allOptions=drop_down.options
print(len(allOptions))
for i in allOptions:
    print(i.text)




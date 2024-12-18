import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

"search on wikipedia by id"
# driver.get('https://www.wikipedia.org/')
# search_box=driver.find_element(By.ID,"searchInput")
# search_box.send_keys('ancient history')
# time.sleep(1)
# driver.find_element(By.CLASS_NAME,'pure-button').click()
# time.sleep(3)

"search on google by name attribute"
# driver.get('https://www.google.com/')
# search_box=driver.find_element(By.NAME,"q")
# search_box.send_keys("python programming language")
# time.sleep(2)
# driver.find_element(By.CLASS_NAME,"gNO89b").click()
# time.sleep(2)


"selenium website to open projects"
# driver.get('https://www.selenium.dev/')
# link=driver.find_elements(By.CLASS_NAME,"nav-item")
# link[3].click()
# time.sleep(2)

"task 4"
# driver.get('https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php')
# placeholder=driver.find_element(By.TAG_NAME,"input")
# print(len(placeholder))

"task 5 web driver opens"
# driver.get('https://www.selenium.dev/documentation/')
# driver.find_element(By.PARTIAL_LINK_TEXT,"WebDriver").click()
# time.sleep(2)






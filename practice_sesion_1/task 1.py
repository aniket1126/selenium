import  time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service



service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

"search on wikipedia by id"
driver.get('https://www.wikipedia.org/')
search_box=driver.find_element(By.ID,"searchInput")
search_box.send_keys('ancient history')
time.sleep(1)
driver.find_element(By.CLASS_NAME,'pure-button').click()
time.sleep(3)
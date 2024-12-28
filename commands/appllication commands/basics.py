"application commands"

# get() -- open the url
# title -- to capture the title of the current webpage
# current url -- to capture the current url of the web page
# page_source -- to capture the source code of the page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service_obj)

driver.get("http://www.automationpractice.pl/index.php")
print(driver.title)
print(driver.current_url)
print(driver.page_source)
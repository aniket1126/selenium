import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


driver.get("http://www.automationpractice.pl/index.php")
time.sleep(3)
#
# search_box=driver.find_element(By.ID,"search_query_top")
# search_box.send_keys("Tshirt")
# time.sleep(2)
# driver.find_element(By.NAME,"submit_search").click()
# time.sleep(2)
# driver.find_element(By.LINK_TEXT,"Faded Short Sleeve T-shirts").click()
# time.sleep(2)
#
# exp_title="Faded Short Sleeve T-shirts - My Shop"
# act_title = driver.title
# if exp_title == act_title:
#     print("test pass")
# else:
#     print("fail")

"number of sliders"
# slider = driver.find_elements(By.CLASS_NAME,"homeslider-container")
# print(len(slider))

"number of images"
# img=driver.find_elements(By.TAG_NAME,"img")
# print(len(img))

"number of links"
# link = driver.find_elements(By.TAG_NAME,"a")
# print(len(link))

"names of categories "
# categories=driver.find_elements(By.CLASS_NAME,"sf-menu")
# print(len(categories))
# for i in categories:
#     print(i.text)


















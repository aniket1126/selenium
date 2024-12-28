import time
from os import times


from Scripts.select import select
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
serviceObj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service = serviceObj)

# driver.get("https://www.hyrtutorials.com/p/frames-practice.html")
# driver.find_element(By.ID,"name").send_keys("aniket")
# frame1=driver.find_element(By.ID,"frm1")
# frame2=driver.find_element(By.ID,"frm2")
#
# driver.switch_to.frame(frame1)
# dropdown = Select(driver.find_element(By.ID,"course"))
# dropdown.select_by_visible_text("Java")
# time.sleep(2)
#
# driver.switch_to.default_content()
# driver.switch_to.frame(frame2)
# driver.find_element(By.ID,"firstName").send_keys("aniket")
# driver.find_element(By.ID,"lastName").send_keys("jangra")
# time.sleep(2)

"EMBEDDED FRAMES"
driver.get("https://demo.automationtesting.in/Frames.html")
driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a").click()
time.sleep(2)
frame1 = driver.find_element(By.XPATH,"//*[@id='Multiple']/iframe")
driver.switch_to.frame(frame1)
frame2 = driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(frame2)
driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("aniket")
time.sleep(2)


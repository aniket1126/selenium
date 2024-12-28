import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
time.sleep(2)

# Locate the "First Name" field using ID
first_name_field = driver.find_element(By.ID,"name").send_keys("aniket")
time.sleep(2)

# Locate the "Gender" radio button using Name
gender_radio_button = driver.find_element(By.NAME,"gender").click()
time.sleep(2)
#
# Locate the "Submit" button using Class Name
submit_button = driver.find_element(By.CLASS_NAME,"btn")
time.sleep(2)

# Locate the "Gender" radio button using XPath
gender_radio_button_xpath = driver.find_element(By.XPATH,"//*[@id='practiceForm']/div[3]/div/div/div[2]/input").click()
time.sleep(2)

# Locate the "First Name" text box using XPath
first_name_xpath = driver.find_element(By.XPATH,"//*[@id='name']")
time.sleep(2)

# Locate the "Current Address" text area using CSS Selector
CurrentAddress_area = driver.find_element(By.CSS_SELECTOR,"textarea[name='picture']").send_keys("ambala city, Haryana")
time.sleep(2)

# Locate the first <input> element using Tag Name
input_element = driver.find_element(By.TAG_NAME,"input")

driver.quit()

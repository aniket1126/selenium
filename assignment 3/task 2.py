import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

driver.implicitly_wait(10)

driver.get("https://www.amazon.com/")

search_bar = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar.send_keys("laptop")
search_button=driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(2)

try:
    search_results = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot .s-result-item")))
    print("Search results loaded")
except Exception as e:
    print("Search results not loaded:", e)
try:
    recommendations = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".a-carousel-viewport")))
    print("Product recommendations loaded")
except Exception as e:
    print("Product recommendations not loaded:", e)

driver.quit()

# Import necessary modules from Selenium
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import  Service

service_obj = Service(r"D:\BEBO\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Step 1: Launch the browser
# Create a new instance of the Chrome browser


# Step 2: Navigate to Amazon website
# Use the 'get' method to navigate to the desired URL
driver.get("https://www.amazon.com")

# Step 3: Verify the title of the page
# Get the title of the page and print it
page_title = driver.title

# Check if the page title matches the expected value
if "Amazon" in page_title:
    print("Title verification successful! The page title is:", page_title)
else:
    print("Title verification failed. The page title is:", page_title)

# Step 4: Close the browser
# Close the browser window
driver.quit()


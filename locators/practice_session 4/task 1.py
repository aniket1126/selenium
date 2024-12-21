from locators.css_selectors.basics import driver

driver.find_element(By.XPATH,"//input[@id='username']//parent::td")

"task 2"
driver.find_element(By.XPATH,"//div[@class='container']//parent::td/child::")

"task 3"
driver.find_element(By.XPATH,"//section[@id='main_content']//descendants::a")

"task 4"
driver.find_element(By.XPATH,"//button[@id='submit']//following-sibling::a")

"task 5"
driver.find_element(By.XPATH,"//label[@for='email']//preceding-sibling::a")



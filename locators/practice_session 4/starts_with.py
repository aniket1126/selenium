driver.find_element(By.XPATH,"//input[starts-with(@user,'em')]")

"task 2"
driver.find_element(By.XPATH,"//div[starts-with(@id,'main-')]")

"MIXED TASKS"
driver.find_element(By.XPATH,"//section[@id,'content']/descendant::*(contains(@class='data']")

"task 2"
driver.find_element(By.XPATH,"//h1[@text()='welcome']/following-sibling::*[starts_with(@class,'header')]")

"task 3"
driver.find_element(By.XPATH,"//div[@class='item container']/following-sibling::*")

"task 4"
driver.find_element(By.XPATH,"//p[@text()='Disclaimer']/ancestors::*")

"task 5"
driver.find_element(By.XPATH,"//input[@starts-with='email']and contains(@class,'input')]")
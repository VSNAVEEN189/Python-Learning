# FIND ELEMENT BY XPATH
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in")

time.sleep(5)

driver.find_element(By.ID, "twotabsearchtextbox").send_keys("iphones")
driver.find_element(By.ID, "nav-search-submit-button").click()

time.sleep(5)

list = driver.find_elements(By.XPATH, "//h2//span")
print(str(len(list)) + " products found")

for i in list:
    print(i.text)

driver.quit()
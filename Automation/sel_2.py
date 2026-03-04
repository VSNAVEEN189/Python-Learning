from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.amazon.in/')

time.sleep(5)

select = driver.find_element(By.PARTIAL_LINK_TEXT, "Mobile")
select.click()

time.sleep(5)

select_1 = driver.find_element(By.PARTIAL_LINK_TEXT, "Audio")
select_1.click()

time.sleep(5)

# Automating the amazon.in page from mobiles->Audio->Exit page

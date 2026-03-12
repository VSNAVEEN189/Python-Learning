from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://automationexercise.com/")
# driver.maximize_window()

wait = WebDriverWait(driver, 4)

# Click Signup / Login
login_page = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Signup / Login"))
)
login_page.click()

# Enter email
email = wait.until(
    EC.presence_of_element_located((By.NAME, "email"))
)
email.send_keys("dummy@email.com")

# Enter password
password = driver.find_element(By.NAME, "password")
password.send_keys("dummy123")

# Click login
driver.find_element(By.XPATH, "//button[text()='Login']").click()

input("Press Enter to close browser...")
driver.quit()
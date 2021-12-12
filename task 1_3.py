from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('http://localhost/litecart/admin/')

driver.find_element_by_name('username').send_keys('admin')
driver.find_element_by_name('password').send_keys('admin')
driver.find_element_by_name('login').click()

try:
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, 'body-wrapper'))
    )
finally:
    driver.quit()
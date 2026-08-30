from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_loc = r"webdrivers\chromedriver-win64\chromedriver.exe"
service = Service(driver_loc)

driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://www.saucedemo.com/")
time.sleep(2)

username = driver.find_element(By.ID, "user-name")
username.send_keys("standard_user")
time.sleep(2)

password = driver.find_element(By.ID, "password")
password.send_keys("secret_sauce")
time.sleep(2)

login_btn = driver.find_element(By.ID, "login-button")
login_btn.click()
time.sleep(2)

print(driver.title)
print(driver.current_url)
time.sleep(1)

driver.quit()
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"webdrivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

time.sleep(2)

print(driver.title)

time.sleep(2)

driver.quit()
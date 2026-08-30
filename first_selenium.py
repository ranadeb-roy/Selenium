from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

service = Service(r"webdrivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.maximize_window()    # full screen

driver.get("https://www.google.com")    # search google
time.sleep(2)

print("Title: ", driver.title)
print("URL: ", driver.current_url)

driver.get("https://www.youtube.com")   # search youtube
time.sleep(2)

print("Title: ", driver.title)
print("URL: ", driver.current_url)

driver.back()   # go back to google
time.sleep(2)

driver.forward()    # go forward to youtube
time.sleep(2)

driver.refresh()    # refresh youtube
time.sleep(2)

driver.quit()
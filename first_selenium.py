from selenium import webdriver
from selenium.webdriver.chrome.service import Service   # used to start a webdriver (e.g. chrome webdriver)
from selenium.webdriver.common.by import By     # used for locators (i.e. ID, CLASS, etc.)
from selenium.webdriver.common.keys import Keys     # used to click keys from the keyboard
import time     # used to stop the script for a specific amount of time using time.sleep()

service = Service(r"webdrivers\chromedriver-win64\chromedriver.exe")

driver = webdriver.Chrome(service=service)
driver.maximize_window()    # full screen

driver.get("https://www.google.com")    # search google
time.sleep(2)

print("Title: ", driver.title)
print("URL: ", driver.current_url)

search_box = driver.find_element(By.NAME, "q")  # find the search box using NAME "q"
search_box.send_keys("Selenium Python")         # type "Selenium Python" in the search box
time.sleep(1)
search_box.send_keys(Keys.ENTER)                # clicks ENTER after typing
time.sleep(5)

# driver.get("https://www.youtube.com")   # search youtube
# time.sleep(2)

# print("Title: ", driver.title)
# print("URL: ", driver.current_url)

# driver.back()   # go back to google
# time.sleep(2)

# driver.forward()    # go forward to youtube
# time.sleep(2)

# driver.refresh()    # refresh youtube
# time.sleep(2)

driver.quit()
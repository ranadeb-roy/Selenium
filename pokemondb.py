# This is a simple script to scrape data from the Pokemon Database website using Selenium.

from selenium import webdriver
import time

driver = webdriver.Edge()

driver.get("https://pokemondb.net/")
driver.maximize_window()
print(driver.title)
time.sleep(3)

driver.quit()
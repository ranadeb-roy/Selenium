# This is a simple script to scrape data from the Pokemon Database website using Selenium.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Edge()

# Navigate to the Pokemon Database website
driver.get("https://pokemondb.net/")
driver.maximize_window()
print(driver.title, "\n")
time.sleep(2)

# Navigate to "Pokemon FireRed & LeafGreen" page
games_menu = driver.find_element(By.XPATH, "/html/body/nav/ul/li[3]/a")
ActionChains(driver).move_to_element(games_menu).perform()
time.sleep(2)
driver.find_element(By.LINK_TEXT, "FireRed & LeafGreen").click()

# Wait until the page is fully loaded
wait = WebDriverWait(driver, 30)    # Wait for max 30 seconds
wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
print(driver.title, "\n")
time.sleep(2)

# Navigate to the Pokedex page
driver.find_element(By.LINK_TEXT, "FireRed & LeafGreen Pokédex").click()
wait.until(lambda driver: driver.execute_script("return document.readyState") == "complete")
print(driver.title, "\n")
time.sleep(2)

# Scrape the data of 10 Pokemons in the Pokedex
info_card = driver.find_elements(By.CLASS_NAME, "infocard")
print(f"Found {len(info_card)} Pokemons in the Pokedex.\n")

pokemon_data = []
for card in info_card:
    id = card.find_element(By.XPATH, "./span[2]/small[1]").text
    name = card.find_element(By.XPATH, "./span[2]/a").text
    types = card.find_element(By.XPATH, "./span[2]/small[2]").text
    pokemon_data.append({"id": id, "name": name, "types": types})

print("First 10 Pokemons in the Pokedex:")
for i in range(10):
    data = pokemon_data[i]
    print(f"Id: {data['id']}")
    print(f"Name: {data['name']}")
    print(f"Types: {data['types']}")
    print("---")

time.sleep(2)

driver.quit()
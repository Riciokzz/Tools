from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


URL = "https://orteil.dashnet.org/experiments/cookie/"


chrome_driver_path = "chromedriver.exe"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(URL)

# Cookie to click
cookie = driver.find_element(By.ID, "cookie")

# Upgrade items ID
items_list = []
for item in driver.find_elements(By.CSS_SELECTOR, "#store div"):
    items_list.append(item.get_attribute("id"))

# Setting time intervals
five_minutes_rule = time.time() + 5 * 60
five_seconds_rule = time.time() + 5


# 5 min loop
while time.time() < five_minutes_rule:
    cookie.click()

    # Every 5 sec loop
    if time.time() > five_seconds_rule:

        # Getting prices from shop
        price_list = []
        items_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        for price in items_prices:
            try:
                cost = int(price.text.split("-")[1].replace(",", ""))
                price_list.append(cost)
            except IndexError:
                pass

        # Creating dict for id and price
        upgrades = {}
        for i in range(len(price_list)):
            upgrades[price_list[i]] = items_list[i]

        # Getting cookie count
        money = int(driver.find_element(By.ID, "money").text.replace(",", ""))

        # Check which upgrades can be brought
        affordable_upgrade = {}
        for cost, item_id in upgrades.items():
            if money > cost:
                affordable_upgrade[cost] = item_id

        # Buying the most expensive upgrade
        most_expensive_upgrade = max(affordable_upgrade)
        #print(most_expensive_upgrade)
        purchase_id = affordable_upgrade[most_expensive_upgrade]
        driver.find_element(By.ID, purchase_id).click()

        # Add 5 sec
        five_seconds_rule = time.time() + 5

time.sleep(50)

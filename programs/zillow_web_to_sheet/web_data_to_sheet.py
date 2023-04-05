from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time


ZILLOW_WEB = "https://www.zillow.com/homes/for_sale/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.74334944677734%2C%22east%22%3A-122.12330855322266%2C%22south%22%3A37.64383227656958%2C%22north%22%3A37.90651729386%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D"
GOOGLE_FORM = "https://docs.google.com/forms/d/e/1FAIpQLSeR7JZ5WO9p9hKuVpOQtF-aTiwfXnOKPXZjr0foL7nfH7yyjQ/viewform?usp=sf_link"


#### Connecting to web ####
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                   "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

# Getting html
response = requests.get(ZILLOW_WEB, headers=headers)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# Getting all links and placing in list
link_all_data = soup.find_all("a", attrs={"class": "StyledPropertyCardDataArea-c11n-8-73-8__sc-yipmu-0 lhIXlm property-card-link"})
all_links = []
for link_data in link_all_data:
    href = link_data["href"]
    all_links.append(href)

# Getting all address and placing in list
address_all_data = soup.find_all("address", attrs={"data-test": "property-card-addr"})
all_address = []
for address in address_all_data:
    all_address.append(address.text)

# Getting all prices and placing in list
prices_all_data = soup.find_all("span", attrs={"data-test": "property-card-price"})
all_prices = []
for price in prices_all_data:
    all_prices.append(price.text)

### Submitting all data to sheet ###

# Installing chrome service
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Looping data to submitting sheet
for data in range(len(all_links)):
    driver.get(GOOGLE_FORM)

    time.sleep(2)
    address_typing = driver.find_element(By.XPATH, "//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
    price_typing = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_typing = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_typing.send_keys(all_address[data])
    price_typing.send_keys(all_prices[data])
    link_typing.send_keys(all_links[data])
    submit_button.click()


##### Check internet speed at speedtest.net and post a tweet in Twitter


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Websites and inputs
SPEED_TEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/i/flow/login"
print("Enter your Twitter details:")
twitter_email = input("Email: ")
twitter_username = input("Username: ")
twitter_pass = input("Password: ")

# Setting up
chrome_driver_path = "chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        # Go to Speedtest
        self.driver.get(SPEED_TEST_URL)
        time.sleep(2)
        # Accept privacy cookies
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)
        # Testing up/down speed
        self.driver.find_element(By.CLASS_NAME, "js-start-test").click()
        # Wait for results
        time.sleep(50)
        self.driver.find_element(By.XPATH, '//*[text()="Back to test results"]').click()
        self.up = self.driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed").text
        self.down = self.driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed").text

    def tweet_at_provider(self):
        self.driver.get(TWITTER_URL)
        time.sleep(3)
        # Login to Twitter, entering Email
        enter_email = self.driver.find_element(By.CLASS_NAME, "r-30o5oe")
        enter_email.send_keys(twitter_email)
        enter_email.send_keys(Keys.ENTER)
        time.sleep(3)
        # Entering username
        enter_username = self.driver.find_element(By.XPATH, '//*[@data-testid="ocfEnterTextTextInput"]')
        enter_username.send_keys(twitter_username)
        enter_username.send_keys(Keys.ENTER)
        time.sleep(3)
        # Entering password
        enter_password = self.driver.find_element(By.XPATH, '//*[@type="password"]')
        enter_password.send_keys(twitter_pass)
        enter_password.send_keys(Keys.ENTER)
        time.sleep(3)
        # Entering the tweet and submitting it
        twit = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
        twit.send_keys(f"Down/Up speed: {self.down}/{self.up} Mbps with Cgates internet.")
        self.driver.find_element(By.XPATH, "//*[@data-testid='tweetButtonInline']").click()
        # Closing program
        self.driver.quit()


bot = InternetSpeedTwitterBot(chrome_driver_path)
bot.get_internet_speed()
bot.tweet_at_provider()

# OLD method

## Go to Speedtest
#driver.get(SPEED_TEST_URL)
#
## # Accept privacy cookies
#time.sleep(2)
#driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
#
## # Testing up/down speed
#time.sleep(2)
#start_test = driver.find_element(By.CLASS_NAME, "js-start-test")
#start_test.click()
#
## # Wait for results
#time.sleep(50)
#driver.find_element(By.XPATH, '//*[text()="Back to test results"]').click()
#down_speed = driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.download-speed").text
#up_speed = driver.find_element(By.CLASS_NAME, "result-data-large.number.result-data-value.upload-speed").text
#
#speed_info = (f"Down/Up speed: {down_speed}/{up_speed} Mbps with Cgates internet.")
#
## Login to Twitter
## Entering email
#driver.get(TWITTER_URL)
#time.sleep(3)
#enter_email = driver.find_element(By.CLASS_NAME, "r-30o5oe")
#enter_email.send_keys(twitter_email)
#enter_email.send_keys(Keys.ENTER)
#time.sleep(3)
#
## Entering username
#enter_username = driver.find_element(By.XPATH, '//*[@data-testid="ocfEnterTextTextInput"]')
#
#enter_username.send_keys(twitter_username)
#enter_username.send_keys(Keys.ENTER)
#time.sleep(3)
#
## Entering password
#enter_password = driver.find_element(By.XPATH, '//*[@type="password"]')
#
#enter_password.send_keys(twitter_pass)
#enter_password.send_keys(Keys.ENTER)
#time.sleep(3)
#
## Entering the tweet and submitting it
#
#twit = driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block.public-DraftStyleDefault-ltr")
#twit.send_keys(speed_info)
#driver.find_element(By.XPATH, "//*[@data-testid='tweetButtonInline']").click()
#
#
#driver.quit()

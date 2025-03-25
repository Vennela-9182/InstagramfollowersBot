from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os
from dotenv import load_dotenv
load_dotenv()
password=os.getenv("password")
email=os.getenv("email")
class InstaFollowers:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/?flo=true")
        sleep(3)
        username = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(1) > div > label > input")
        username.send_keys()
        sleep(1)
        password = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div.x9f619.xjbqb8w.x78zum5.x168nmei.x13lgxp2.x5pf9jr.xo71vjh.xqui205.x1n2onr6.x1plvlek.xryxfnj.x1c4vz4f.x2lah0s.xdt5ytf.xqjyukv.x1qjc9v5.x1oa3qoh.x1nhvcw1 > div:nth-child(2) > div > label > input")
        password.send_keys()
        password.send_keys(Keys.ENTER)
        sleep(1)

    def find_followers(self):
        sleep(5)
        self.driver.get("https://www.instagram.com/pythonlearnerr/")
        sleep(5.2)

        # XPath to open followers popup
        modal_xpath = "//a[contains(@href, '/followers/')]/span"
        followers_button = WebDriverWait(self.driver, 12).until(EC.presence_of_element_located((By.XPATH, modal_xpath)))
        followers_button.click()

        # Improved method to wait for the popup
        followers_popup = None
        for _ in range(5):  # Retry a few times in case of failure
            try:
                followers_popup = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]"))
                )
                break
            except:
                sleep(1)  # Wait a bit and retry

        if not followers_popup:
            print("❌ Failed to locate the followers popup.")
            return

        # Keep the popup open by scrolling
        for _ in range(10):  # Adjust the scroll attempts as needed
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_popup)
            sleep(2)

        # Find follow buttons
        follow_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Follow')]")

        for button in follow_buttons:
            try:
                # Move to button before clicking
                ActionChains(self.driver).move_to_element(button).perform()
                sleep(1)

                # Click the button
                button.click()
                sleep(2)  # Delay to avoid detection
            except Exception as e:
                print(f"Error clicking follow button: {e}")

        print("✅ All follow buttons clicked.")


bot = InstaFollowers()
bot.login()
bot.find_followers()
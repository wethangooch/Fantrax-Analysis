from selenium import webdriver
import time

# Set up Chrome WebDriver (replace with the actual path to your chromedriver)
chrome_driver_path = '/chromedriver'

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the Fantrax login page
driver.get("https://www.fantrax.com/fantasy/league/login")

input("Log in and then click enter")



# Once logged in, capture the cookies
cookies = driver.get_cookies()
print(cookies)



driver.quit()


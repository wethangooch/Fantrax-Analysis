from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time



chrome_options = Options()


# Hide "DevTools listening" and other ChromeDriver logs
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# Optional: run ChromeDriver itself in "silent" mode
chrome_options.add_argument("--log-level=3")  # Only fatal errors


# Initialize the Chrome WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open the Fantrax login page
driver.get("https://www.fantrax.com/fantasy/league/login")

# Create a WebDriverWait with timeout (e.g., 20 seconds)
wait = WebDriverWait(driver, 20)


login_button = wait.until(
    EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/fx-nav/nav-general-menu/section[1]/a[2]'))
)

login_button.click()

input("Log in and then click enter")


# Once logged in, capture the cookies
cookies = driver.get_cookies()
print(cookies)



driver.quit()


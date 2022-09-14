from selenium import webdriver
import os
os.system("pip install webdriver-manager")

# import module for downloading latest ChromeDriver:
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()

# disable browser notifications
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# Uncomment this line if site isolation is causing bugs, see for more details: 
# https://www.chromium.org/Home/chromium-security/site-isolation/
# chrome_options.add_argument("--disable-site-isolation-trials")  

# Downloads the latest version of ChromeDriver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

with open("urls.txt", "r") as urls_file:
    # Remove blank lines
    urls = (url.rstrip() for url in urls_file)
    urls = list((url for url in urls if url))

    # Open the URLs
    for url in urls:
        driver.get(url)

        # Insert tasks you wish to automate using Selenium, for instance:
        # clicking through a required dialog (ad block prompts, cookie settings, etc.)
        # navigating to a specific subpage or accessing a link
        # etc.

        # Open new tab and make it the active tab
        driver.execute_script("window.open('https://www.google.com');")
        driver.switch_to.window(driver.window_handles[-1])        


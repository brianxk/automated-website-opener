from selenium import webdriver


# Disable notifications popup
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)

# Provide path to chromedriver.exe and initialize driver
chromedriver_path = "./chromedriver.exe"
driver = webdriver.Chrome(chromedriver_path, options=chrome_options)

with open("urls.txt", "r") as urls_file:
    # Remove blank lines from file
    urls = (url.rstrip() for url in urls_file)
    urls = list((url for url in urls if url))

    # Open the urls
    for url in urls:
        driver.get(url);

        # Open new tab and make it the active tab
        driver.execute_script("window.open('https://www.google.com');")
        driver.switch_to.window(driver.window_handles[-1])

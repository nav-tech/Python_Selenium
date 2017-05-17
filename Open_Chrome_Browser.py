from selenium import webdriver
import time
driver = webdriver.Chrome("/Users/AbhinavPrasad/Downloads/chromedriver")
driver.get("https://www.google.com/")
print(driver.current_url)
print(driver.title)
time.sleep(5)
driver.quit()
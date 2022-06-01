from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome("chromedriver.exe", options=options)
url = 'https://www.youtube.com/watch?v=kWiCuklohdY'
driver.get(url)

last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

while True:
    driver.execute_script("window,scrollTo(0, document.documentElement.scrollHeight);")
    time.sleep(0.5)
    new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    if new_page_height == last_page_height:
        break
    last_page_height = new_page_height

html_source = driver.page_source

# html_source.append(html_source)
print("ok")

driver.quit()
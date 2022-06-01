import re
from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

driver.close()

soup = BeautifulSoup(html_source, 'lxml')

youtube_user_IDs = soup.find_all('h3', 'style-scope ytd-comment-renderer')
# youtube_comments = soup.find_all('yt-formatted-string', 'style-scope ytd-comment-renderer')

str_youtube_userIDs = []
# # str_youtube_comments = []

for i in range(1, len(youtube_user_IDs)):
    str_youtube_userIDs.append(re.sub('\n', ' ', (str(youtube_user_IDs[i].text))))


# for i in range(1, len(youtube_comments), 2):
#     str_youtube_comments.append(str(youtube_comments[i].innerText))
# def test(youtube_user_IDs):
#     hangul = re.compile('[^ ㄱ-ㅣ가-힣+]')



print(str_youtube_userIDs[0:10])
# print(list(youtube_comments)[0:10])
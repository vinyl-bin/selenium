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
# 1단락 끝
#youtube_user_IDs = soup.select('div#header-author > a > span')
youtube_user_IDs = soup.find_all('h3', 'style-scope ytd-comment-renderer')
youtube_comments = soup.find_all('yt-formatted-string', 'style-scope ytd-comment-renderer')
#youtube_comments = soup.select('yt-formatted-string#content-text')
# 2 단락 끝
str_youtube_userIDs = []
str_youtube_comments = []

for i in range(1, len(youtube_user_IDs)):
    str_youtube_userIDs.append(str(youtube_user_IDs[i].text))

for i in range(1, len(youtube_comments)):
    str_youtube_comments.append(str(youtube_comments[i].text))

print(str_youtube_userIDs[0:10])
print(str_youtube_comments[0:10])
# for i in range(len(youtube_user_IDs)):
#     str_tmp = str(youtube_user_IDs[i].text)
#     #   print(str_tmp)
#     str_tmp = str_tmp.replace('\n', '')
#     str_tmp = str_tmp.replace('\t', '')
#     str_tmp = str_tmp.replace('                 ', '')

#     str_youtube_userIDs.append(str_tmp)

#     str_tmp = str(youtube_comments[i].text)
#     str_tmp = str_tmp.replace('\n', '')
#     str_tmp = str_tmp.replace('\t', '')
#     str_tmp = str_tmp.replace('                 ', '')

#     str_youtube_comments.append(str_tmp)
# # 3단락 끝
# for i in range(len(str_youtube_userIDs)):
#     print(str_youtube_userIDs[i], str_youtube_comments[i])
# # 4단락 끝
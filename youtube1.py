from selenium import webdriver as wd
from bs4 import BeautifulSoup
import time
import urllib.request
import urllib.parse  #plusUrl을 변환시켜주기 위해


url = 'https://www.youtube.com/watch?v=fwlztjjWfUo'

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(id = 'yt-formatted-string')

print(title)

# for i in title:
#     print(i.text)            #이건 모든 i정보에서 텍스트만 가져오는 거여서 .text를 붙여준다.
#     # print(i.attrs['href'])   #attrs가 []안에 있는 속성을 가져온다
#     print()

# driver = wd.Chrome(executable_path="chromedriver.exe")
# url = 'https://www.youtube.com/watch?v=kWiCuklohdY'
# driver.get(url)

# last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

# while True:
#     driver.execute_script("window,scrollTo(0, document.documentElement.scrollHeight);")
#     time.sleep(3.0)
#     new_page_height = driver.execute_script("return document.documentElement.scrollHeight")

#     if new_page_height == last_page_height:
#         break
#     last_page_height = new_page_height

# html_source = driver.page_source

# driver.close()

# soup = BeautifulSoup(html_source, 'lxml')
# 1단락 끝


import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='api_txt_lines total_tit _cross_trigger')

for i in title:
    print(i.text)            #이건 모든 i정보에서 텍스트만 가져오는 거여서 .text를 붙여준다.
    print(i.attrs['href'])   #attrs가 []안에 있는 속성을 가져온다
    print()
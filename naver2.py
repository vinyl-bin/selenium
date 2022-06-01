import urllib.request
import urllib.parse  #plusUrl을 변환시켜주기 위해
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query='
plusUrl = input('검색어를 입력하세요: ')
print()
url = baseUrl + urllib.parse.quote_plus(plusUrl)  #plusUrl을 변환시켜줌(영어는 변환안해도 잘 실행됨 아스키코드 어쩌구 때문에;;)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='api_txt_lines total_tit _cross_trigger')

for i in title:
    print(i.text)            #이건 모든 i정보에서 텍스트만 가져오는 거여서 .text를 붙여준다.
    print(i.attrs['href'])   #attrs가 []안에 있는 속성을 가져온다
    print()

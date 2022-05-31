import urllib.request
import urllib.parse  #plusUrl을 변환시켜주기 위해
from bs4 import BeautifulSoup
import csv

baseUrl = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=view&query='
plusUrl = input('검색어를 입력하세요: ')
url = baseUrl + urllib.parse.quote_plus(plusUrl)  #plusUrl을 변환시켜줌(영어는 변환안해도 잘 실행됨 아스키코드 어쩌구 때문에;;)

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='api_txt_lines total_tit _cross_trigger')

for i in title:
    a = (i.text)            
    b = (i.attrs['href'])   
    c = ()

 
f = open('data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
for line in rdr:
    print(line)
f.close()    

????????
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from time import sleep
import requests
import re
import pandas as pd
import numpy as np
import os

from selenium.webdriver.common.keys import Keys

import warnings
warnings.filterwarnings('ignore')

name=['비눗방울']
category=['리뷰']

#비눗방울 리뷰
ns_address="https://search.shopping.naver.com/catalog/32312940336?query=%EB%B9%84%EB%88%97%EB%B0%A9%EC%9A%B8&NaPm=ct%3Dl3wbhe7k%7Cci%3Db1e4a573a939efb90f075e283fc583cf80e1ce6a%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D74e479a60372823701768de0d2a5983ab4cde64e"
#xpath
shoppingmall_review="/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[4]/ul"

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

header = {'User-Agent': ''}
d = webdriver.Chrome('chromedriver',options=options) # webdriver = chrome
d.implicitly_wait(3)
d.get(ns_address)
req = requests.get(ns_address,verify=False)
html = req.text 
soup = BeautifulSoup(html, "html.parser")
sleep(2)

#쇼핑몰 리뷰 보기
d.find_element_by_xpath(shoppingmall_review).click()
sleep(2)

element=d.find_element_by_xpath(shoppingmall_review)
d.execute_script("arguments[0].click();", element)
sleep(2)

def add_dataframe(reviews,stars,cnt):  #데이터 프레임에 저장
    #데이터 프레임생성
    df1=pd.DataFrame(columns=['review','star'])
    n=1
    if (cnt>0):
        for i in range(0,cnt-1):
            df1.loc[n]=[reviews[i],stars[i]] #해당 행에 저장
            i+=1
            n+=1
    else:
        df1.loc[n]=['null','null']
        n+=1    
    return df1

d.find_element_by_xpath(shoppingmall_review).click() #스크롤 건드리면 안됨
# name_=name[0]
# category_=category[0]
reviews=[]
stars=[]
cnt=1   #리뷰index
page=1

while True:
    j=1
    print ("페이지", page ,"\n") 
    sleep(2)
    while True: #한페이지에 20개의 리뷰, 마지막 리뷰에서 error발생
        try:
            star=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[4]/ul/li['+str(j)+']/div[1]/span[1]').text
                       
            stars.append(star.strip("평점"))
            review=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[4]/ul/li['+str(j)+']/div[2]/div[1]').text
            reviews.append(review)
            if j%2==0: #화면에 2개씩 보이도록 스크롤
                ELEMENT = d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[4]/ul/li['+str(j)+']/div[2]/div[1]')
                d.execute_script("arguments[0].scrollIntoView(true);", ELEMENT)       
            j+=1
            print(cnt, review ,star, "\n")
            cnt+=1 
        except: break
            
    sleep(2)
    
    if page<11:#page10
        try: #리뷰의 마지막 페이지에서 error발생
            page +=1
            next_page=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[4]/div[3]/a['+str(page)+']').click() 
            
        except: break #리뷰의 마지막 페이지에서 process 종료
        
    else : 
        try: #page11부터
            page+=1
            if page%10==0: next_page=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[4]/div[3]/a[11]').click()
            else : next_page=d.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[2]/div[3]/div[4]/div[3]/a['+str(page%10+2)+']').click()
            
        except: break
            

df4=add_dataframe(reviews,stars,cnt)
#save()

df4.to_csv('naverforsenti2.txt')
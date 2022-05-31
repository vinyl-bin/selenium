from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
# from user_agent import generate_user_agent, generate_navigator
# import requests

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
# url ='https://www.coupang.com/vp/products/6383116177?itemId=13570926430&vendorItemId=5284384578&sourceType=srp_product_ads&clickEventId=f2b5b010-a87e-407b-ab24-3a957cd9b183&korePlacement=15&koreSubPlacement=1&isAddedCart=#sdpReview'
# html = requests.get(url, headers = headers).text

# print(generate_user_agent(device_type='desktop'))
# print(generate_user_agent(os='win', device_type='desktop'))
# print(generate_user_agent(os=('mac', 'linux'), device_type='desktop'))
# navigator = generate_navigator()
# print(navigator)
# print(navigator['platform'])
driver=webdriver.Chrome("chromedriver.exe")
driver.get('https://www.coupang.com/vp/products/6383116177?itemId=13570926430&vendorItemId=5284384578&sourceType=srp_product_ads&clickEventId=f2b5b010-a87e-407b-ab24-3a957cd9b183&korePlacement=15&koreSubPlacement=1&isAddedCart=#sdpReview')
time.sleep(3)

# query_text='에어팟프로'

element=driver.find_elements_by_class_name('sdp-review__article__list__review__content js_reviewArticleContent')
# # headerSearchKeyword : 검색창 ID
# element.send_keys(query_text)
# element.submit()
# time.sleep(1)

f = open("C:/Users/강다빈/Desktop/jocoding selenium/새파일2.txt", 'w')
f.write(element)
f.close()
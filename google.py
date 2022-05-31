from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
#이때 7분 50초쯤 cd selenium실행할때 다른 터미널로 들어가서 해줘야함!!!!!!!!!!!!
driver = webdriver.Chrome()
driver.get("http://inc.sungkyul.ac.kr/")
# elem = driver.find_element_by_class_name("swiper-slide-image")
# elem.send_keys("조코딩")
# elem.send_keys(Keys.RETURN)
# driver.find_elements_by_css_selector(".rg_i.Q4LuWd")[0].click() #[0]은 가장 첫번째꺼를 끄집어서 클릭하겠다는 뜻이다.
time.sleep(5)
# print(driver.find_element_by_class_name("swiper-slide-image")[0].get_attribute("src")) #이부분이 막힘ㅠㅠ
# print(driver.find_elements(by=By.CLASS_NAME, value="swiper-slide-image")[1].get_attribute('src'))


f = open("C:/Users/강다빈/Desktop/jocoding selenium/새파일.txt", 'w')
arr = [i.get_attribute('src') for i in driver.find_elements(by=By.CLASS_NAME, value="swiper-slide-image")]
data = '\n'.join(arr)
f.write(data)
f.close()




# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()


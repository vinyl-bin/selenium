from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome("chromedriver.exe", options=options)
driver.get('https://movie.naver.com/movie/bi/mi/review.naver?code=74977')
time.sleep(3)

f = driver.find_element(by=By.TAG_NAME, value="strong").get_attribute('innerText')
print(f)

# print(driver.find_elements(by=By.XPATH, Value="//*[@id="review_1078666"]/div[1]/div/div[4]/div")) 
# f = driver.find_elements_by_xpath("/html/body/div[4]/div/div[2]/div/ul/li[2]/div[1]/div/div[4]/div")
# print(f)

# print(driver.find_elements(by=By.CLASS_NAME, value="swiper-slide-image")[1].get_attribute('src'))

# f = open("C:/Users/강다빈/Desktop/jocoding selenium/새파일.txt", 'w')
# arr = [i.get_attribute('src') for i in driver.find_elements(by=By.CLASS_NAME, value="swiper-slide-image")]
# data = '\n'.join(arr)
# f.write(data)
# f.close()


# element=driver.find_elements_by_class_name('review_list_v2__message js-collapsed-review-content js-translate-review-message')
# arr = [i.get_attribute('src') for i in driver.find_elements(by=By.CLASS_NAME, value="review_list_v2__message js-collapsed-review-content js-translate-review-message")]
# print('\n'.join(arr))

# # f = open("C:/Users/강다빈/Desktop/jocoding selenium/새파일2.txt", 'w')
# f.write(element)
# f.close()
'''
Created on 2020. 8. 25.

@author: GDJ24
화면  이미지 저장하기
'''

from selenium import webdriver
url = "http://www.naver.com/"
driver = webdriver.Chrome("C:/20200224/setup/chromedriver")
driver.get(url)
#open된 브라우저의 화면을 이미지로 저장하기
driver.save_screenshot("naverhome.png")
driver.quit()
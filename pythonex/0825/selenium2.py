'''
Created on 2020. 8. 25.

@author: GDJ24
네이버 로그인하기
'''
import time
from selenium import webdriver

driver = webdriver.Chrome("C:/20200224/setup/chromedriver")
time.sleep(1)
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com")
id = input("네이버 아이디를 입력하세요: ")
driver.execute_script("document.getElementsByName('id')[0].value='"+id+"'")
pw = input("네이버 비밀번호를 입력하세요: ")
driver.execute_script("document.getElementsByName('pw')[0].value='"+pw+"'")
driver.find_element_by_xpath('//*[@id="log.login"]').click()

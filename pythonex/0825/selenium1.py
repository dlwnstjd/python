'''
Created on 2020. 8. 25.

@author: GDJ24
셀레니움 예제
'''

from selenium import webdriver  #pip install selenium
import time
#chromedriver.exe 파일 다운 로드:
#    http://chromedriver.chromium.org/downloads
#    크롬의 버전에 맞는 파일 다운받기. 크롬도움말 -> 크롬 정보
#D:/20200224/setup/chromedriver => 위치에 chromedriver.exe 파일 복사
driver = webdriver.Chrome("C:/20200224/setup/chromedriver")
driver.get("http://python.org")
#menus: link 목록을 가진 li 태그들 선택
menus = driver.find_elements_by_css_selector('#top ul.menu li')
print(type(menus))
pypi = None
for m in menus:
    if m.text == "PyPI":
        pypi = m
    print(m.tag_name,m.text)
pypi.click()    #클릭
time.sleep(5)   #5초 대기
driver.quit()   #브라우저 종료
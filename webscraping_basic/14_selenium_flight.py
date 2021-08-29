from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url 로 이동

# 가는 날 선택
elem = browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]")
elem.click()

# 스크롤 내리기
browser.execute_script("window.scrollTo(0, 540)")

# 날짜 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[5]/button").click()
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[5]/td[1]/button").click()

# 출발지 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]").click()
browser.find_element_by_link_text("국내")
browser.find_element_by_link_text("인천").click()

# 도착지 선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]/b").click()
browser.find_element_by_link_text("유럽").click()
browser.find_element_by_link_text("프랑크푸르트").click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()


# # 가는 날 선택 클릭
# browser.find_element_by_link_text("가는날 선택").click()


# # 이번 달 25일 28일 선택
# # browser.find_elements_by_link_text("25")[0].click() # [0] -> 이번 달
# # browser.find_elements_by_link_text("28")[0].click() # [0] -> 이번 달

# # 다음 달 25일 28일 선택
# browser.find_elements_by_link_text("25")[0].click() # [0] -> 이번 달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음 달

# # 출발지 파리 선택
# browser.find_element_by_xpath("//*[@id='l_1']/div/div[1]/a[2]").click()
# browser.find_element_by_xpath("//*[@id='l_1']/div/div[1]/div[2]/table[6]/tbody/tr[1]/td[1]/a").click()

# # 도착지 인천 선택
# browser.find_element_by_xpath("//*[@id='l_1']/div/div[2]/a[2]").click()
# browser.find_element_by_link_text("인천").click()

# # 항공권 검색 클릭
# browser.find_element_by_link_text("항공권 검색").click()

try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[3]/div[1]/div[7]/ul/li[1]")))
    # 성공했을 때 동작수행
    print(elem.text)
finally:
    browser.quit()

# 첫번째 결과 출력
elem = browser.find_element_by_xpath("//*[@id='content']/div[3]/div[1]/div[7]/ul/li[1]")
print(elem.text)
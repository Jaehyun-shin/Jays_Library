# Quiz) 부동산 매물 - 송파 헬리오시티 정보를 스크래핑하는 프로그램을 만드시오
# 
# [조회 조건]
# 1. "http://daum.net" 접속
# 2. '송파 헬리오시티' 검색
# 3. 다음 부동산 부분에 나오는 결과 정보
# 
# [출력 결과]
# print("="*10, "매물", i, "="*10) -> for schleife i 
# print(f"거래 :{매매종류}")
# print(f"면적 :{면적},{공급/전용}")
# print(f"가격 :{가격}, (만원)")
# print(f" 동: {동호수}")
# print(f" 층: {고/23}") 

from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = "http://daum.net"
browser.get(url)

# 송파 헬리오시티 입력
browser.find_element_by_id("q").send_keys("송도 동일하이빌 파크포레")

# 검색 버튼 누르기
browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]").click()

# 부동산 사이트 열기
browser.find_element_by_xpath("//*[@id='estateColl']/div[2]/div/div[2]/div[1]").click()

# 옆의 스크롤 내리기 - 먼저 클릭 후 스크롤 내리기
browser.find_element_by_xpath("//*[@id='__next']/div[2]/div/div[2]/div/div/div[1]/div[2]/div[2]/div/div[5]/div/div[1]/div[2]/div/div[2]").click()
browser.execute_script("window.scrollTo(0, 100)")
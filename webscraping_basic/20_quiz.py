import requests
from bs4 import BeautifulSoup

url_weather = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hfZrWsprvhGssQbHmJVssssssX8-228724"
res_weather = requests.get(url_weather)
res_weather.raise_for_status()

soup_weather = BeautifulSoup(res_weather.text, "lxml")

# url_IT_news = "https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=105"
# res_IT_news = requests.get(url_IT_news)
# res_IT_news.raise_for_status()

# soup_IT_news = BeautifulSoup(res_IT_news.text, "lxml")

# url_Hackers = ""
# res_Hackers = requests.get(url_Hackers)
# res_Hackers.raise_for_status()

# soup_Hackers = BeautifulSoup(res_Hackers.text, "lxml")

weather = soup_weather.find("div", attrs={"class":"today_area _mainTabContent"})

curr = weather.find("p", attrs={"class":"info_temperature"}).get_text()

min = weather.find("span", attrs={"class":"min"}).get_text()
max = weather.find("span", attrs={"class":"max"}).get_text()

rain = soup_weather.find("div", attrs={"class":"table_info weekly _weeklyWeather"}).find("ul", attrs={"style":"display: block;"})


# rain_morning = soup_weather.find("li", attrs={"class":"date_info today"}).find("span", attrs={"class":"rain_rate wet"}).get_text()
# rain_afternoon =  soup_weather.find("li", attrs={"class":"date_info today"}).find("span", attrs={"class":"rain_rate"}).get_text()

# print(weather.find("p", attrs={"class":"cast_txt"}).get_text())
# print("현재 : {}{}".format(curr, " (최저 "+min+" / 최고 "+max+")"))
# print("오전{} / 오후{}".format(rain_morning, rain_afternoon))
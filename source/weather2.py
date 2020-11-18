from selenium import webdriver
from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject

path = "C:/Users/marsh/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)  # 브라우저를 켜는 함수

driver.implicitly_wait(10)
driver.get(
    "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%98%84%EC%9E%AC%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery=%ED%98%84%EC%9E%AC+%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&tqi=UJRvUsprvhGssgA2scKssssstlC-201880")
weather_infos = driver.find_elements_by_css_selector(
    '#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info')
mise_infos = driver.find_elements_by_css_selector(
    '#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info')


def weather_all:
    for weather_info in weather_infos:
        now_temp = weather_info.find_element_by_css_selector(
            '#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > p > span.todaytemp').text
        now_temp_kor = weather_info.find_element_by_css_selector(
            '#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-child(1) > p').text
        now_rain = weather_info.find_element_by_css_selector(
            '#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-child(3) > span').text
        low = weather_info.find_element_by_css_selector(
            '#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-child(2) > span.merge > span.min > span').text
        high = weather_info.find_element_by_css_selector(
            '#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.main_info > div > ul > li:nth-child(2) > span.merge > span.max > span').text

        print(now_temp, now_temp_kor, now_rain, low, high)

    for mise_info in mise_infos:
        mise_all = []
        mise = mise_info.find_element_by_css_selector(
            '#main_pack > section.sc_new.cs_weather._weather > div > div.api_cs_wrap > div.weather_box > div.weather_area._mainArea > div.today_area._mainTabContent > div.sub_info > div > dl > dd.lv2 > span.num').text
        mise_all.append(mise)
        if mise >= 0 and mise <= 30:
            mise_all.append('좋음!')


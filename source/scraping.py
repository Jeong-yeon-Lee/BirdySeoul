from selenium import webdriver
from pymongo import MongoClient  # pymongo를 임포트 하기

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.myproject

path = "C:/Users/marsh/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)  # 브라우저를 켜는 함수


def print_park(park_name):
    driver.implicitly_wait(10)
    driver.get(f"http://parks.seoul.go.kr/parks/list.do?searchWd={park_name}&searchTp=park")
    # park_info = []
    # park_info=driver.find_element_by_css_selector('.mopark_cont')

    name_element = driver.find_element_by_css_selector( '#app > ul > li > div.mopark_cont > div.info_txt.w_calc > h3 > a').text
    print(name_element)
    address_element = driver.find_element_by_css_selector('#app > ul > li > div.mopark_cont > div.info_txt.w_calc > div:nth-child(2) > p').text.replace('오시는 길', '')
    print(address_element)
    phone_element = driver.find_element_by_css_selector('#app > ul > li > div.mopark_cont > div.info_txt.w_calc > div:nth-child(3) > p').text
    print(phone_element)

    info= {
                'name':name_element,
                'address': address_element,
                'phone': phone_element,
            }
    # park_info.append(info)
    return info



park_info_list= print_park('명일근린공원')

db.park_info.insert_one(park_info_list)
import requests
from bs4 import BeautifulSoup

open_url='http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1114052000'

res=requests.get(open_url)
soup=BeautifulSoup(res.content,'html.parser')

data=soup.find_all('item')

def get_weather():
    for item in data:
        weather=item.find_all('wfkor')
        today_now=weather[-1]
        return today_now
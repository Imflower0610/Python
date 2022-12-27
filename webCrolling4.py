import bs4
import urllib
from urllib.request import urlopen

# 시간대별 날씨
url = "https://weather.naver.com/today/07140535?cpName=KMA"
html = urlopen(url)
bsp = bs4.BeautifulSoup(html,"html.parser")
findth = bsp.findAll("th",{"class","data top _cnItemTime"})
timeList =[]
whetherInfo =[]
whetherList = dict()

for th in findth:
   time = th.find('span').text
   timeList.append(time)

for th in findth:
    info = th.find('i').text
    po = dict()
    po={"날씨": info}
    whetherInfo.append(po)

whetherList = dict(zip(timeList,whetherInfo))
print(whetherList)
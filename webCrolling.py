
# HTTP - 하이퍼텍스트(html)을 전송하기 위한 규칙
# 프로토콜 - 약속, 규약
# URL - http://www.naver.com
# URI - url에 사용자 정보와 스키마를 포함한 값

# 스크래핑 - 웹페이지에서 자동으로 데이터를 추출하는것,웹 페이지 소유자의 허락없이
#           무단으로 끌어오는 행위 
# 크롤링 - 웹페이지에서 자동으로 데이터를 추출

# 스크래핑은 특정 웹사이트에서 데이터 추출, 크롤링은 웹사이트의 링크를 통해서 정보를 
# 찾아서 추출하는 방식 - 둘다 데이터를 추출한다라는 것이 동일하기에 흔히 크롤링이라고 한다.

# import urllib.request
# import requests

# 웹을 만들기 위해 사용되는 다양한 기술들
# 필수- HTTP(HTTPS → SSL/TLS) : HTML과 JS와 CSS같은 파일을 웹 서버에게 요청하고 받아오는 프로토콜
#     - HTML : 웹 페이지를 채울 내용
#     - Javascript : 웹 페이지에 들어갈 기능
#     - CSS : 웹 페이지를 예쁘게 꾸밀 디자인
#     - ASP/SAP.NET, JSP, PHP : 웹 서버 페이지를 만드는 기술들
#     - JSP
#     - PHP
#     - DB
# 선택- Python
#     - Spring
#     - Jquery
#     - Ajax

# 해싱 : 내가 원하는 데이터만 뽑아오기
# Beautifulsoup4 = 파싱을 편리하게 할 수 있는 일종의 라이브러리
# urllib 안에 request 안에 있는 urlopen을 임포트해서 사용하겠다
from urllib.request import urlopen
import bs4

# test_html = "<html><head></head><Body><div>hahaha</div>"
# test_html += "<p> jgl babo</p></Body></html>"
# bobj = bs4.BeautifulSoup(test_html,"html.parser")

# print(test_html)
# print(bobj)
# print(test_html.find("div"))
# print(bobj.find("div"))
# print(bobj.find("p"))
#url = "http://www.naver.com"
#html = urlopen(url)

#print(html.read())

html ="""
<html>
    <body>
        <div>
            <ul class = "kjy">
                <li>babo</li>
                <li>19</li>
            </ul>
            <ul class ="ljh">
                <li>babo</li>
                <li>old</li>
            </ul>
        </div>
    </body>
</html>
"""
bsp = bs4.BeautifulSoup(html, "html.parser")
# 태그의 속성을 통해서 가져오는 방법
ul = bsp.find("ul",{"class":"ljh"})
print(ul)

# li = bsp.findAll("li")
# print(li[1])

# for i in li:
#     print(i.text)

# url = "https://www.naver.com" #naver url 저장
# html = urlopen(url)#url open
# html = html.read()# naver sorce 읽기
# print(html)

# bsp = bs4.BeautifulSoup(html, "html.parser")
# temp = bsp.findAll("strong",{"class","current"})
# print(temp)
# # 현재기온 몇도인것만 출력하려면?
# print(temp[0].text)
# for t in temp:
#     if "현재기온" in t:
#         print(t.text)


# nav = bsp.findAll("a",{"class","nav"})
# for n in nav:
#     print(n.text)


# url = "https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y&aid=0013655846" 
# html= urlopen(url)
# html = html.read()

# bsp = bs4.BeautifulSoup(html, "html.parser")
# news_ul = bsp.find("ul",{"class","type02"})
# print(len(news_ul)) # 길이가 1로 찍히면 하나라는 거니까 find로 바꿔줌
# news_li = news_ul.findAll("li")
# for li in news_li:
#     strong = li.find("strong")
#     print(strong.text)

# 내가푼거
# url = "https://comic.naver.com/webtoon/weekdayList?week=thu"
# html= urlopen(url)
# html = html.read()

# bsp = bs4.BeautifulSoup(html, "html.parser")
# thu_title = bsp.find("ul",{"class","img_list"})
# print(len(thu_title)) 
# thudt = thu_title.findAll("dt")
# for dt in thudt:
#     thu_dt = dt.find("a")
#     print(thu_dt.text)

# 쌤이 푼거
# url = "https://comic.naver.com/webtoon/weekday"
# html= urlopen(url)
# html = html.read()

# bsp = bs4.BeautifulSoup(html, "html.parser")
# div = bsp.findAll("div",{"class","col_inner"})
# ul = div[3].find("ul")
# lis = ul.findAll("li")
# for li in lis:
#     title = li.find("a",{"class","title"})
#     print(title.text)

url = "https://www.op.gg/statistics/champions"
html= urlopen(url)
html = html.read()

bsp = bs4.BeautifulSoup(html, "html.parser")
body = bsp.find("tbody")
td = body.findAll("td")
print(td)
for r in td:
    td = r.find("div", {"class","css-qzg52u e1alsbyt0"})
    print(td)
    # div = td.find("div",{"class","css-qzg52u e1alsbyt0"})
    # if int(div.text)>50:
    #     jjang = td.find("strong")
    #     print(jjang.text)
# lis = ul.findAll("li")
# for li in lis:
#     title = li.find("a",{"class","title"})
#     print(title.text)

 
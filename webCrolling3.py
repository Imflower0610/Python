
# 이름, 가격 불러오기
# import requests
# import bs4

# url = "https://www.therosebay.co.kr/shop/big_section.php?cno1=1004"
# res = requests.get(url=url)

# bsp = bs4.BeautifulSoup(res.content,"html.parser")
# names = bsp.findAll("p",{"class","name"})
# price = bsp.findAll("span",{"class","p_value"})

# item=[]
# for i in range(len(names)):
#     name = names[i].find("a").text
#     p= price[i].find("strong").text
#     item.append([name,p])
# print(item)

import requests
import bs4
import urllib
from urllib.request import urlopen
import pymysql

#데이터 베이스 연결
conn = pymysql.connect(host ='127.0.0.1', user='root', password = 'Wkwmdsk18!', db='kr',charset='utf-8')
#데이터베이스 연결 후에 커서 생성, 커서는 파이썬과 DB 사이를 연결해주는 드라이버의 형태
#커서생성
cur = conn.cursor()

# 쇼핑몰에서 이름 가져오기
url = "https://www.graychic.co.kr/product/list.html?cate_no=4"
#res = requests.get(url =url)
html = urlopen(url)

bsp = bs4.BeautifulSoup(html,"html.parser")
href_list= []
items = bsp.findAll("div",{"class","sp-product__thumb"})
for item in items:
    href_list.append( item.find("a")['href'])

site="https://www.graychic.co.kr"
#여기부터가 하나 인덱스 바꿔서 하면 됨 => 반복문 돌려야됨
#파이썬에서는 try-catch가 아니라 try-except가 예외처리문임
item_list = dict() # 제품의 상세 정보 저장 딕셔너리(key-상품명, value-정보)


for i in range(len(href_list)):
    href= urllib.parse.quote(href_list[i]) #한글을 인코딩
    item_link = site + href  #제품 상세페이지 주소

    item_html = urlopen(item_link)  # 제품 상세페이지 html

    item_bsp = bs4.BeautifulSoup(item_html,"html.parser") #제품상세페이지 파서


    item_name='' #제품명
    info_t = item_bsp.select_one("#gc_de_sizeinfo")

    info_tr = info_t.select("tr")
    th_list=[]  
    td_list=[]
    try:
        for tr in info_tr:
            try:
                th=tr.select_one("th").text
                td = tr.select_one("td").text
            except Exception as e:
                continue
            else:
                if '상품명'==th:
                    item_name=td
                else:
                    th_list.append(th)
                    td_list.append(td)
    except Exception as e:
        print("몇번 째 제품 오류 :"+ str(i))

    size_t = item_bsp.select_one("#gc_de_sizecm")
    size_th = size_t.select("th")
    for th in size_th:
        th_list.append(th.text)
    size_td = size_t.select("td")
    for td in size_td:
        td_list.append(td.text)

    item_list[item_name] = dict(zip(th_list,td_list))


cur.execute("insert into outers values('" +"word"+"')")
print( item_list)


# find -> tag로 찾기, # select -> css 선택자로 찾기
# find -> 태그 1개찾기 # findAll -> 태그 여러개 
# select -> 선택자에 해당하는 모든 태그 # selectOne -> 1개 태그
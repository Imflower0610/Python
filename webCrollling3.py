
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
from urllib.request import urlopen

url = "https://www.graychic.co.kr/product/list.html?cate_no=4"
html = urlopen(url)

bsp = bs4.BeautifulSoup(html,"html.parser")
href_list =[]
items = bsp.findAll("div",{"class","sp-product__thumb"})
for item in items:
    href_list.append(item.find("a")["href"])
    
site = "https://www.graychic.co.kr"
print(href_list)




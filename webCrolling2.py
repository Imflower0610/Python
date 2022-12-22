import bs4
import requests
url = "https://ethereum.org/ko/"

result = requests.get(url=url)

bsp = bs4.BeautifulSoup(result.content,"html.parser")

main_ul = bsp.find("ul",{"class","e1p6yfdy3"})

print(main_ul)

main_li = main_ul.findAll("li",{"class","e1oznup73"})

href_list=[]

for li in main_li:
    sub_ul = li.find("ul")
    sub_li = sub_ul.findAll("li")
    for sli in sub_li:
        href_list.append(sli.find("a")['href'])

# nav = bsp.findAll("nav")
# if len(nav)==1:
#     mul = nav.find("ul")
#     print(mul)
# else:
#     nav = bsp.find("nav",{"class","e1p6yfdy7"})
#     mul = nav.find("ul")
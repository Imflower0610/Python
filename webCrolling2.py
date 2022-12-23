import bs4
import requests

def getHref(html_tag):
    mul = bsp.find("ul",{"class","permanent-list-body"})
    href_list =[] 

    ali = mul.findAll("li")
    for a in ali:
        sul = a.findAll("ul",{"class","permanent-area"})
        for li1 in sul:
            li = li1.findAll("li")
            for li_1 in li:
                if li_1.find("a"):
                    href_list.append(li_1.find("a")['href'])

    return href_list

url = "https://www.museum.go.kr/site/main/content/permanent_exhibition_guide"
site = "https://www.museum.go.kr"
result = requests.get(url=url)

bsp = bs4.BeautifulSoup(result.content,"html.parser")

href_list = getHref(bsp)
site_info =dict()
dic_column = ["title","menu"]
for href in href_list:
    link = site + href
    result2 = requests.get(url=link)
    sub_bsp = bs4.BeautifulSoup(result2.content,"html.parser")
    ptitle = sub_bsp.find("h2",{"class","page-title"}).text
    showtitle = sub_bsp.find("p",{"class","showroom-title"}).text
    ul = sub_bsp.find("ul",{"class","swiper-wrapper"})
    li = ul.findAll("li")
    menu =[l.find("a").text.strip() for l in li ]
    site_info[ptitle] = dict(zip(dic_column,[showtitle,menu]))
    # print(menu)
print(site_info)

  


# main_ul = bsp.find("ul",{"class","e1p6yfdy3"})

# print(main_ul)

# main_li = main_ul.findAll("li",{"class","e1oznup73"})

# href_list=[] # 저장할 리스트 

# for li in main_li:
#     sub_ul = li.find("ul")
#     sub_li = sub_ul.findAll("li")
#     for sli in sub_li:
#         href_list.append(sli.find("a")['href'])

# nav = bsp.findAll("nav")
# if len(nav)==1:
#     mul = nav.find("ul")
#     print(mul)
# else:
#     nav = bsp.find("nav",{"class","e1p6yfdy7"})
#     mul = nav.find("ul")
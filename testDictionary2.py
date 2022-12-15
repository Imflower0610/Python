"""
파이썬 기초 + 딕셔너리


파이썬 데이터 타입
 : 리스트, 튜플, 딕셔너리, 셋, 배열

"""

import random
# 각 도시의 신생아 초등학생, 중학생, 고등학생, 대학생, 노년층 인구수를 입력하여
# 딕셔너리에 저장
# 어떤 것이 키이고 어떤것이 value로 들어가야할지 생각해보기

# 내가 푼거
city = ("서울",'대전','대구','광주','부산','울산','세종')
keys = ["신생아", "초등학생","중학생", "고등학생", "대학생", "노년층"]
values = list() 
dicCity = dict()

for i in range(len(city)):
    temp = list() 
    for k in keys: 
       temp.append(input(city[i] + k))
    values.append(temp)

for v in city:
    for i in values:
        dicCity[v] = dict(zip(keys,i))
print(dicCity)


# 쌤이 푼거
city = ("서울",'대전','대구','광주','부산','울산','세종')
kind = ("신생아", "초등학생","중학생", "고등학생", "대학생", "노년층")

population = dict()
for cname in city:#도시수만큼 입력하기
    temp = dict()
    print("======== {0} 지역 인구수 ========".format(cname))
    for k in kind:
        i = input(cname+k)
        print("{0} : {1} 명".format(k,i))
        temp[k]=i #신생아, 초등학생, 중학생,,, 인구수를 딕셔너리에 저장
        #키 - 신생아, 초딩, 중딩..., value = 인구수
    population[cname] = temp #위에서 만들어진 딕셔너리를 value로 도시이름은 key로

for k in population:
    print("{0} : {1}".format(k, population))

"""
파이썬 기초 + 딕셔너리


파이썬 데이터 타입
 : 리스트, 튜플, 딕셔너리, 셋, 배열

"""
"""
# 딕셔너리 : 사전
# 파이썬 딕셔너리 == 자바 Map
# 'key : value'의 구조로 이루어져 있다.

# 딕셔너리도 셋처럼 중괄호로 나타내지만 key와 value값이 필요하기 때문에 2개의 데이터를 하나로 묶어서 표시한다.
dic = {'이름':'이순신','나이':24,'직업':'군인'}
print(dic)
print(dic['이름']) # key를 입력하면 이에 맞는 데이터가 출력됨

# key로 사용가능 - 문자열, 정수, 실수, 불(True,False)
# key로 사용불가 - 리스트, set, 딕셔너리
# value 사용 - 아무거나 다 가능

# 딕셔너리 생성방법
# 방법1. 그냥 중괄호만 치면 셋 아니고 딕셔너리로 인식
dic = {}
dic1 = dict(이름='김지연',나이=29,직업='마이쮸판매원')
print(dic1)

# 방법2. 딕셔너리 생성
dic = dict()
dic2 = dict([('이름','이지현'),('age',26),('특징','알면서')])

# 방법3. key 따로 value 따로// 리스트를 딕셔너리로 바꿀 때
dic3 = dict(zip(['이름','나이','관심분야'],['윤재영',25,'컴퓨터선생님']))
print(dic3)

print(dic3['이름'])
dic3['관심분야']='지연이누나'
print(dic3)

dic3['싫어하는것']='옆반선생님'
print(dic3)

if '이름' in dic3:
    print("너의 이름은 : {0}".format(dic3['이름']))
else:
    print("존재하지 않는 키입니다.")

#딕셔너리 키 몇개?
print(len(dic3))

#리스트를 딕셔너리로 입력하기
title = ["캐릭터명","생명력","코딩기술","잔머리","수학능력","공간능력","지능지수"]
data = []
for x in title:
    data.append(input(x + ":"))
# print(data)
info = dict(zip(title,data))
print(info)

#반복문 이용해서 출력하기
for x in info:
    print(x) # dictionary key 출력

for x in info:
    print(info[x]) # dictionary value 출력

for x in info.values():
    print(x) # dictionary value 출력

for x in info.keys():
    print(x) # dictionary key 출력

for k, v in info.items():
    print(k,v) # dictionary key, value 모두 출력
"""
title = ["이름","키","몸무게","관심분야"]
# 5명의 정보를 입력한다.
info =[]
for i in range(5):
    data =[]
    for t in title:
        data.append(input(t + ":"))
    info.append(data)

# 이름을 키로 사용하여 딕셔너리에 5명의 정보를 저장하시오
dic_info = dict()
for data in info:
    dic_info[data[0]] = dict( zip(title,data) )
print(dic_info)
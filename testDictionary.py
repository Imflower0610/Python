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

#이름, 번호,c언어성적,java성적,react성적,db성적,지적수준
#10명의 성적을 딕셔너리에 저장하세요

keys = ["이름","번호","C언어성적","자바성적","react성적","DB성적","지적수준"]
values = list() #입력한 값을 리스트에 저장하고 그 리스트를 저장할 리스트
for i in range(2):
    temp = list() # 입력한 값이 저장될 리스트
    for k in keys: # 한명에 대한 정보입력 for문
       temp.append(input(k))
    values.append(temp) 

class501 = dict()
for v in values:
    class501[v[0]] = dict(zip(keys,v))# 딕셔너리 이름을 key, 모든 데이터를 value

for k in class501:
    print("{0}:{1}".format(k,class501[k]))

# 위 내용을 토대로 입력한 성적들의 평균점수(지적수준빼고)를 구하여 
# 이름은 key, value는 평균점수와 지적수준을 딕셔너리에 저장
# 첫번째 방법
avg = list()
dic_avg = dict()
for name in class501: # name에는 키로사용한 이름이저장
    sum = 0
    for title in class501[name]: # title에는 이름, 번호, 성적들,
        if title =="이름" or title =="번호" or title =="지적수준":
            continue
        sum = sum +int(class501[name][title])
    
    dic_avg[name] = dict(평균점수 = sum/4, 지적수준 = class501[name]['지적수준'])
print(dic_avg)


# 딕셔너리의 key만 리스트로 변환
    #  li = list(dict.keys())
# 딕셔너리의 value만 리스트로 변환
    #  li = list(dit.values())
# 딕셔너리의 key, value를 리스트로 변환
    #  li - list(dic.items())
# key와 value를 한쌍으로 튜플형태로 저장
    # [('k1':'v1'),('k2':'v2')]

#두번째 방법
avg = list()
dic_avg = dict()
for name in class501: # name에는 키로사용한 이름이저장
    sum=0
    title = list(class501[name].keys()) 
    for i in range(2,6):
        sum = sum + int(class501[name][title[i]]) 
    dic_avg[name] = dict(평균점수 = sum/4, 지적수준 = class501[name]['지적수준'])
print(dic_avg)

#세번째 방법
avg = list()
dic_avg = dict()
for name in class501: # name에는 키로사용한 이름이저장
    sum=0
    score = list(class501[name].values())
    for i in range(2,6):
        sum = sum + int(score[i])
    dic_avg[name] = dict(평균점수 = sum/4, 지적수준 = class501[name]['지적수준'])
print(dic_avg)
"""
# 문의제목, 작성자, 문의내용, 작성일, 답변, 답변일
# 딕셔너리에 저장하는데 키는 번호를 사용, 파일에서 읽어드린 순서대로 1번부터 부여

info = ["문의제목", "작성자", "문의내용", "작성일", "답변", "답변일"]
file=[]
with open("c:/test/question.txt","r",encoding="utf-8") as f:
    file = f.readlines()
for i in range(len(file)):
    file[i] = file[i][:len(file[i])-1] # 엔터문자 빼려고 -1
    file[i] = file[i].split(" ") # file의 i번째 인덱스를 띄어쓰기 기준으로 잘라서 배열로 저장 => 여기서부턴 2차원배열임

quest = dict()
for f in range(len(file)):
    quest[f+1]= dict(zip(info,file[f]))

for k in quest:
    print("{0}:{1}".format(k,quest[k]))

# 문의목록을 출력하시오(번호와 제목, 작성일만)
# 보고싶은 문의번호를 입력하면 아래와 같이 출력
# 출력예시
# 작성자 : 윤재명
# 제목 : 출마선언합니다.
# 작성일 : 2027-03-10
# 문의글 : 대선출정하고싶습니다.도와주세요.
# ============================================
# 답변 : 1억 있어요?
# 답변일 : 2027-02-05

# search = input("문의번호 :")
# for s in quest:
#     if str(s) == str(search) :
#         qus = []
  

for num in quest:
    print("{0}. {1} {2}".format(num, quest[num]["문의제목"],quest[num]["작성일"]))

번호 = int(input("문의번호 :"))
print("작성자 : {0} \n제목 : {1} ".format(quest[번호]['작성자'],quest[번호]['문의제목']))
print("\n작성일 : {0} \n문의글 : {1}".format(quest[번호]['작성일'],quest[번호]['문의내용']))
print("\n===============================\n답변 :{0}  \n답변일 : {1}".format(quest[번호]['답변'],quest[번호]['답변일']))

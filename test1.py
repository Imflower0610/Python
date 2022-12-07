# 출력 - print()
# 입력 - input()
# 변수 - num=10 그냥 타입없이 변수만
# 타입변환 - str() 문자열, int() 정수, float()실수
# 출력포멧 - print("{0}".format(10) ), print("{0} {1}".format(10,"변수정"))

#문제1.
# 시속 v km/h로 달리고 있는 자동차가 반지름 r km인 원형트랙을 달리고 있다면 한바퀴 완주하는데 걸리는 시간은 몇분인가?
# 둘레 = 반지름 * 2파이 
# 거리 = 속력*시간 => 시간 = 거리/속도

v = int(input(" 자동차의 시속을 입력하세요 : "))
r = int(input(" 원형트랙의 반지름을 입력하세요 :"))

dist = r*2*3.14 # 트랙길이
time = dist/v *60 # 분으로 나타내야 하니까 *60

print("완주 시간{0}분".format(time)) #print("완주시간 : " + str(time))


#문제2.
# 소주 한잔에 수명이 2분 단축된다.
# 지연이가 소주를 20년동안 마셨다.
# 그렇다면 지연이는 수명이 총 몇분/몇 시간/며칠 줄었을까?

drink = int(input("하루에 소주를 몇잔 마셨는가? : "))
soju = drink*2
year = 365*20
min = soju*year
hour = min/60
day = hour/24

print("줄어든 수명은 {0}분".format(min), "{0}시간".format(hour), "{0}일".format(day)+" 입니다.")



# 파이썬에서는 변수를 한 줄에 저장할  수 있다. => 변수타입이 필요하지 않기 때문에 가능하다
x,y,z = "김지연","장영주","변수정"
a=b=c="연하남친"
favorite = ["목발","선인장","19남친"] #리스트
a,b,c = favorite
print(a)
print(b)
print(c)

""" 
    같다 => ==
    같지않다 => !=, >, <, >=, <=
"""
   
num=19
num1=27

# 파이썬에서는 중괄호 없고 대신 콜론(:)이랑 들여쓰기로 if문 만듦!
if num1>num :
    print("누난 내 여자이니까!") #중괄호를 안쓰는 대신 안쪽으로 들어가 있어야 if문 내용으로 인식함
else:
    print("누나 늙었어...")
print("여기는 그냥 출력")

if num1 > num:
    print("연하가 좋아")

age = 22

if age> num :
    print("내가 형이니까 내가 가질게 누나")
elif num>age : #elseif == elif
    print("내가 더 연하야!")
else :
    print("둘 다 싫어! 난 이제 연상좋아!")

name = "김지연"

#한줄if문
print("미안합니다. 그만할게요") if name=="김지연" else print("농일세") if num!=27 else print("뻥인데 계속할건데")

# 문제3
# 지연이가 기원이가 오락실에 갔다
# 둘이 펀치게임을 했다
# 둘의 점수가 각각 얼마인지 입력하여 주가 이겼는지 출력

origin = int(input("기원이의 점수 : "))
delay = int(input("지연이의 점수 : "))

if origin>delay:
    print("기원이가 이김")
elif delay>origin:
    print("지연이가 이김")
else:
    print("둘이 비김")

# 문제 4
# 영주, 지연, 수정이 시험봄
# 세명의 시험점수를 입력하고 등급 출력하기(평균등급)
# 90점 이상 A 80점 이상 B 70점 이상은 C 나머지는 쯧쯧...

young = int(input("영주 점수 : "))
kite = int(input("지연 점수 : "))
modify = int(input("수정 점수 : "))
total = young+kite+modify
avg = total/3
if avg>=90:
    print("평균 등급은 A")
elif avg>=80:
    print("평균 등급은 B")
elif avg>=70:
    print("평균 등급은 c")
else:
    print("쯧쯧....")

#예습해보기 
'''
함수 만들기 : def
파이썬에서 변수 만들 때 맨 앞글자는 영어,한글,_만 허용한다
'''

def score(x,y):
    if x>=90:
        print(y+"의 등급은 A")
    elif x>=80:
        print(y+"의 등급은 B")
    elif x>=70:
        print(y+"의 등급은 c")
    else:
        print("쯧쯧....")

score(kite,"지연")
score(young,"영주")
score(modify,"수정")


#반복문
i=1
while i <=10:
    print(i)
    i+=1 #파이썬은 증산연산자없기 때문에 직접 적어주어야한다.
    
#구구단 4단 출력하기
#4*1=4의 형태로 출력
j=1
while j<10:
    print("4 * "+str(j) +" = " +str(j*4))
    # print("4 * {0} = {1}".format(j,4*j))
    j+=1

i=1
while i<5 :
    print(i)
    i+=1
else:
    print("5보다 크면 반복문 종료됨")

i=1
while True:
    print(i)
    if i==100 :break #반복문 멈출 때
    i+=1

# while문 마지막 무제
# 배꼽지연이가 버스를 타려고 교통카드를 10000원 충전하였다
# 지연이가 버스를 몇번 탈 수 있는가? 잔액은 얼마인가? 버스요금은 1200원이다.
money = 10000
fee = 1200
i=0
while True:
    i+=1
    money -= fee
    if money<fee:break
print("버스는 {0}번 탈 수 있고, 잔액은 {1}원입니다".format(i,money))

for i in range(1, 10, 3): # 1부터 10까지 3씩 반복해라 == 1,4,7 == 3번 반복
    print(i)

for i in range(1,10):
    print("8 * {0} = {1}".format(i,i*8))

#45부터 109까지 출력
for i in range(45,110):
    print(i)

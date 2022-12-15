"""
파이썬 기초 + 리스트


파이썬 데이터 타입
 : 리스트, 튜플, 딕셔너리, 셋, 배열

"""

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
#1부터 100까지 출력하는데 3의 배수에서는 윤재영 출력 
#5의 배수에서는 바보 출력

#내가푼거
for i in range(1,101):
    if i%3==0 and i%5==0:
        print("윤재영 바보")
    elif i%3==0:
        print("윤재영")
    elif i%5==0:
        print("바보")
    else:
        print(i)

#쌤이 푼거
for i in range(1,101):
    if i%3==0:
        print("윤재영", end="")
    if i%5==0:
        print("바보")
    else:
        print(i)


#파이썬 데이터 타입
#리스트, 튜플, 딕셔너리, 셋, 배열

#리스트
name = ["장영주바보","김지연똥개","윤재영멍청이"]

data1 = ["김깅원원장", 100, 3.14, True]

data2 = list(("최윤도서관","변수정과",100))

print(data2[0])
print(data2[-1]) #-1이면 0에서 한칸 뒤니까 맨 마지막인100출력

data3 = ["이종빈티지","윤종찬양하라","이지현미밥맛있어","장영주모"]
print( data3[1:3] )
print(data3[:3])
print(data3[2:])

data3.append("김지연기하네")
data3.append("윤재영영사랑해")
print(data3)

#데이터 삭제하기
#1.실데이터를 통해 삭제
data3.remove("장영주모")
print(data3)

#2.마지막 데이터 삭제
data3.pop()
print(data3)

#3.인덱스 통해 삭제
del data3[2]
print(data3)

#4.리스트 완전삭제
data3.clear()
print(data3)

memo = ["나", "김지연","은","19세 남친을","원한다"]
for me in memo:
    print(me, end="")

#memo의 3번째 인덱스열을 바꾼다
memo[3] = "대머리 남친을"
print()
for me in memo:
    print(me, end="")

#메모의 1, 2, 3번째 인덱스를 바꾼다
memo[1:4] = ["장영주","는","목발을"]
print()
for me in memo:
    print(me,end="")

#3번째 인덱스 자리에 추가
memo.insert(3, "드러운 어그와")
print(memo)

#리스트 합치기
memo1 =["이종빈","윤재영", "변수정"]
memo2 =["장영주부","김지연세많음","이지현왕언니"]
memo1.extend(memo2)
print(memo1)
#리스트 크기
print(len(memo1))

#리스트 생성
#1.memo =["a","b","c"]
#2.memo =["장","영","주","땡"]
#데이터추가 memo.append("리정수")
#데이터 삽입 memo.insert(2,"김민정수리")
#데이터 삭제
#삭제데이터 지정 memo.remove("땡")
#마지막데이터 삭제 memo.pop
#인덱스로 삭제 del memo[3]
#리스트 합치기 memo.extend(리스트)
#리스트 크기 len()
#갯수 구하기 장이라는 데이터가 몇개 있나? -> memo.count("장")
#인덱스 탖기 영이라는 데이터는 몇번 인덱스인가? -> memo.index("영")
#정렬 오름차순 memo.sort() 내림차순 memo.sort(reverse=True)
#반전 memo.reverse()

info501 = ["장영주는 폭력적이다.", "김지연은 연하만좋아한다", "윤재영은 옆반쌤좋아한다.","최윤도는 영주불행이 행복이다.","변수정은 생일이라 코딩이싫데.. ", "종빈이는 지금 게임한다"]

#501호 딸기반 학생이름을 input으로 입력받기
#info501에 해당 학생이름이 있다면 학생의 정보를 출력

name = input("이름을 입력하세요 : ")
for i in range(len(info501)):
    if name in info501[i]:
       print(info501[i])

for info in info501:
    if name in info:
        print(info)

#문제2 info501에서 좋아한다 문구가 있는 정보들 모두 출력
for i in info501:
    if "좋아한다" in i:
        print(i)
        
num=[x for x in range(10)]
print(num)

"""
함수
 1. 자바의 메서드
    @반환타입 메서드(매개변수){메서드 실행내용; 반환타입 있다면 return;}

 2. 자바스크립트 합수
    fucntion 함수이름(매개변수){함수실행내용; 반환값 있다면 return;}

 3. 파이썬 함수
    #def 함수이름(매개변수):
    정의된 함수 실행방법 -> 함수이름()

"""
import random


def sum(a,b):
    return a+b

res = sum(10,20)
print(res)

def func():
    print("나 함수다")

func()

def func1(word):
    print(word +"이다.")

func1("난 바보")

def minus(num1,num2):
    print(num1-num2)

minus(30,15)

def whoami(name,what):
    if name=="장영주":
        print(name +"은,는" +what +"이다")
    else:
        print(name +"은,는" +what +"아니다")

whoami("장영주","바보")
whoami("김지연","바보")

def count(i):
    return i+1

cnt=0
while cnt<10:
    cnt = count(cnt)

print(cnt)

cnt1=0 # 전역변수 count2보다 먼저 생성한다.

def count2():
   global cnt1 # 파이썬의 전역변수 - count2함수에서 cnt1을 사용하고자 한다면 global 붙여서
               # 전역변수임을 알려주고 사용한다. 
               # 전역변수는 최소한으로만 사용 = 코드의 유지보수를 어렵게 만들기 때문!
   cnt1+=1

while cnt1<10:
    count2()
print(cnt1)

# 문제1. 정수 하나를 입력 받아서 함수를 통해 해당 정수의 값을 100 증가시키고 출력하기

def add100(n): # 100이 증가하는 함수 정의 : 지정된 값 100 증가해야 되니까 매개변수 필요
    print(n+100) # 100 증가시키고 출력하기

num =int(input("정수를 입력하세요")) # 정수 입력받기
add100(num) # 100 증가 시켜주는 함수 호출하여 입력받은 숫자를 함숭에 넘겨주기

# 첫번째 할것. 정수 두개 입력받기(변수 두개해서 입력받기)
# 두번째 할것. 정수 입력받는 코드 위에 함수만들기
#             함수의 내용은 두숫자를 곱해서 출력하는 내용
# 세번째 할것. 정수 입력받는 코드 밑에 함수 호출하기

def nbyn(n1,n2):
    print(n1*n2) 

num1 = int(input( "정수를 입력하세요 "))
num2 = int(input( "정수를 입력하세요 "))
nbyn(num1,num2)

# 리스트 만들어서 50까지 짝수만 저장하고 함수에 입력된 숫자에 1 더해서 출력 히스트 반복문으로 함수 호출
# 내가 푼거
evenList =[]
for i in range(1,51):
    if i%2==0:
        evenList.append(i)
def oddNum(n):
    print (n+1)
for i in evenList:
    oddNum(i)

#쌤이 푼거
def add1(n):
    print(n+1)
li = [i for i in range(1,50) if i%2==0]

for i in li:
    add1(i)


# 세 과목 점수를 입력받아서 총점과 평균을 구할 것
#score =[]
#subj=['국어 점수', '영어 점수','물리치료']
#for sub in range(len(subj)):
#    score.append(int(input(subj[sub])))

# 함수로 바꾸기
def score_input(s):
    scr=[]
    for sub in range(len(s)):
        scr.append(int(input(s[sub])))
    return scr # for문으로 입력한 점수가 저장된 리스트 scr을 돌려보내야 한다.
               # 그래야 실 사용하고자 하는 곳에서 값을 사용하니까
def total(점수들): #총점계산함수
    tot =0
    for i in 점수들 : tot += i
    return tot

def avg(총점): # 평균계산함수
    평균 = 총점/3
    print("총점 : {0}, 평균 : {1}".format(총점,평균))
score =[]
subj=['국어 점수', '영어 점수','물리치료']

score = score_input(subj) #튜플로 subj를 함수에 보낸다. subj의 주소를 보내는 것
tot = total(score)
avg(tot)

# 장영순, 김지언, 이지형의 키를 입력하여 총점과 평균을 구하시오

# 내가 푼거
# 작은 키 구하기 함수
def smaller(a,h):
    small =[]
    for i in h:
        if int(h[i])<a:
            small.append(i)
    print("키가 평균보다 작은 사람은 "+ str(small))

# 평균키 함수
def highAvg(s):
    sum =0
    for i in s:
        sum += int(s[i])
    avg = sum/3
    print("평균키는 " +str(avg))
    smaller(avg,s)

# 키 입력
def high_input(name):
    data = []
    for x in name:
        data.append(input(x + ":"))
    info = dict(zip(name,data))
    highAvg(info)

name = ['김지언','이지형','장영순']
high = high_input(name)

#전역튜플
cutegirl =('김지언','이지형','장영순')

# 쌤이 푼거
def small(avg, tall):
    global cutegirl # 전역튜플을 사용하기 위해 global을 해준다.
    for i in range(len(tall)):
        if avg > tall[i] :
            print("평균보다 작은 사람 :{0}".format(cutegirl[i]))

def tall_avg(tall):
    sum = 0
    for 소녀키 in tall : 
        sum += 소녀키
    avg = sum/len(tall)
    print("평균키는 " +str(avg))
    small(avg, tall)

def tall_input():
    global cutegirl # 전역튜플을 사용하기 위해 global을 해준다.
    tall =[]
    for 소녀 in cutegirl:
        tall.append(int(input(소녀)))
    tall_avg(tall)

tall_input()

# 간단한 문제
# 리스트에 1~50까지 저장하기
# 리스트에 저장되어있는 숫자들 중에 5의 배수만 추력
# 5의 배수를 찾아서 출력하는 함수

def fic(li):
    for i in li:
        if i%5==0 : print(i)

li =[i for i in range(1,51)]
#li = []
#for i in range(1,51):
#    li.append(i)
fic(li)

#=============================
def func(a,b,c): 
    print(a)
func(a="abc", b="b", c="c")

#=============================
def func1(national = "계림국"):#매개변수 값이 없으면 계림국
    print(national)

func1("대한민국")
func1()

#===============================
def func2(**info): #arguments 문제는 매개변수 문제
    print(info["name"]) # 매개변수에 ** 들어있으면 키랑 밸류값으로 넣어줘야함! 여러개 넣어도 상관없음

func2(name ="장영주", 상태 = "천재,아름다움,귀여움" )

#첫번째 리스트에는 이순신, 장영실, 정몽주, 정도전, 이성계, 이방지의 키를 입력
#두번째 리스트에는 몸무게를 입력
#키가 가장 작은 사람, 몸무게가 가장 많이 나가는 사람 찾기

#내가 푼거
hero = ("이순신","장영실","정몽주","정도전","이성계","이방지")

def small(high):
    global hero
    out=500
    res =[]
    for i in range(len(hero)):
        if high[i] < out : out = high[i] 
    for i in range(len(hero)):
        if out == high[i]:
            res.append(hero[i])
    print("가장 키가 작은 사람 : " + str(res))

def heavy(w):
    global hero
    out=0
    res =[]
    for i in range(len(hero)):
        if w[i] > out : out = w[i] 
    for i in range(len(hero)):
        if out == w[i]:
            res.append(hero[i])
    print("가장 무거운 사람 : " + str(res))
high = []
weigh = []
for i in hero:
    high.append(int(input(i +" 키를 입력하세요")))
    weigh.append(int(input(i +" 몸무게를 입력하세요")))

small(high)
heavy(weigh)

#쌤이 푼거

옛사람 = ("이순신","장영실","정몽주","정도전","이방지","이성계")

def small_tall(tall):
    global 옛사람
    sm=tall[0]  #0인덱스의 키가 가장 작든 크든 아무상관없음, 비교값이 필요하니 넣어준거
    for i in range(len(tall)): # 키가 가장작은 키 찾기
        if sm > tall[i]:
            sm = tall[i]
    print("키가 작은 사람 : {0}".format(옛사람[tall.index(sm)]))

def high_wd(wd):
    global 옛사람
    hg=wd[0]
    for i in range(len(wd)):
        if hg < wd[i]:
            hg = wd[i]
    print("몸무게가 가장 높은 사람 : {0}".format(옛사람[wd.index(hg)]))


tall = [random.randint(157,184) for i in range(6)]
wd = [random.randint(61,87) for i in range(6)]
print(tall, wd)
small_tall(tall)
high_wd(wd)
"""
파이썬 기초 + 리스트


파이썬 데이터 타입
 : 리스트, 튜플, 딕셔너리, 셋, 배열

"""
import random

name =["김유신", "이순신", "어영담", "이성계", "장영실","홍길동", "김지연", "김춘추"]
job =["군인", "국회의원", "과학자", "도둑","건설업자","밸리댄서","변호사"]
age=[24,35,37,21,54,41,29,35,42]

info =[]

for i in range(10):
    info.append([random.choice(name),random.choice(job),random.choice(age)])

print(info)

# info 리스트로 작업하기
# 1. 직업이 군인인 사람은 누구인지 이름출력
# 2. 직업이 과한자인 사람들의 평균나이 출력
# 3. 나이가 이십대인 사람들의 직업은 무엇인지 출력하기

# 내가 푼 것
so = []
sc = 0
countsc=0
_20 = []

for i in info:
    if i[1]=="군인":
        so.append(i[0])
    if i[1]=="과학자":
        sc+= i[2]
        countsc+=1
    if i[2]>=20 and i[2]<30:
       if i[1] not in _20:
         _20.append(i[1])
if not so : 
    so.append("없음")
if not _20 : 
    _20.append("없음")
print("군인 : ", str(so) )
if countsc != 0:
    print("과학자 평균나이 : ", str(sc/countsc))
else:
    print("과학자가 없다")
print("20대 직업 : ", str(_20))

# 쌤이 푼 것
for people in info:
    if "군인" in people :
        print(people[0])

age =0
cnt =0
for people in info:
    if "과학자" in people:
        age += people[2]
        cnt += 1
if cnt != 0:
    print("과학자 평균 나이 : ", str(age/cnt))
else:
    print("과학자가 없다")

for people in info:
    if int(int(people[2])/10)==2 :
        print(people[1])


#랜덤 사용방법
# rando.randint(1,40) -> 1~40 중 랜덤

a=[] #1~30
b=[] #10~50
c=[] #1~100

num=[]
#a,b,c 리스트에 각각 15개씩 랜덤 범위에 맞춰서 저장하기
#a,b,c 리스트의 값 중에서 중복인 값만 찾아서 num 리스트에 저장하기

#내가 푼 것
for i in range(15):
    a.append([random.randint(1,30)])
    b.append([random.randint(10,50)])
    c.append([random.randint(1,100)])

num2 = a+b+c
for i in num2:
    if i not in num:
        num.append(i)
num.sort()
print(num)

#쌤이 푼 것
for i in range(15):
    a.append([random.randint(1,30)])
    b.append([random.randint(10,50)])
    c.append([random.randint(1,100)])

for x in a: # a리스트에 x값을 저장
    if x in b: # x변수의 값이 b에도 있나
        if x in c: #a와 b에 있는 값이 c에도 있나
            num.append(x)
if len(num) !=0: #len(num) -> num 리스트의 크기값 0이라면 없다, not num -> num이 빙었다면 false
    print(num)
else:
    print("num은 비었다")



word = ["boy", "table", "book", "girl","interest", "limit", "endless", "mission",
"hopi", "tigerprint"]

eng =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

# eng 리스트의 알파벳을 무작위 조합해서 word의 단어중 1개이상 나오는 경우
# 몇번째 조합에서 나오는지 출력
com =""
cnt=0
  
while True:
    for i in range(random.randint(3,10)):
        com += random.choice(eng)
    cnt += 1
    if com not in word:
        com = ""
    if com in word: break
print(com, cnt)

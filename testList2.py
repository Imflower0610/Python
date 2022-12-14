"""
파이썬 기초 + 리스트


파이썬 데이터 타입
 : 리스트, 튜플, 딕셔너리, 셋, 배열

"""
import random

#랜덤 범위 정해서 랜덤값 구하기
num = random.randint(1,45)
print(num)

fristname = ["김","장","이","최","윤","변"]
middle =["기","지","영","윤","재","종","수","민","다"]
last =["원","연","현","영","도","똥","순","숙"]

a = random.choice(fristname)
b = random.choice(middle)
c = random.choice(last)
print(a,b,c)

info = [["김기원","콘샐러드","시험"],["이지현","나이","민감"],["김지연","배꼽","선생님배꼽찔러봄"],
["장영주","바르보사","공통점"],["윤재영","비니","강균성"],["리정수","군대","인민군"]]

#2차원 리스트
for i in info: # i변수에는 info리스트에서 1차원 리스트만 저장
    for k in i: # k변수에는 i에 저장된 리스트 중에서 하나씩 저장
        print (k)

# 문제 3. 위 info리스트에는 이름, 특징1, 특징2 저장되었다
# 이름 또는 특징을 입력받아서 해당 특징을 가진 사람의 이름을 출력하시오
char = input("이름이나 특징을 입력하세요 : ")
for i in info:
    for k in i :
        if char in k:
            print(i[0])

info =[["김민서","군인",28],["정다현", "디자이너", 45], ["장영주", "트럭기사", 61],
["김지연","벨리댄서",34],["윤재영","수필가",58],["최윤도","모필가",24],
["변수정","멕시코음식전문점사장",33],["이종빈","프로게이머연습상대",39],
["윤종찬","서린파이터",22],["이지현","뒷방호랭이",69],["이정수","초딩",11],
["김민정","헤어디자이너조수",28]]

#문제4. 나이대 별로 몇명인지 구하여 출력
#       30대 사람들의 직업만 출력
#       가장 나이 많은 사람의 이름과 직업 출력

age=[0,0,0,0,0,0,0]
age30=[]
oldest = ""
max=0

for i in info:
    age[int(i[2]/10)] += 1 #계산식을 인덱스로 활용가능
    if i[2]>=30 and i[2]<40:
        age30.append(i[1])
    if max<i[2]:
        max=i[2]
        oldest=i
print(age)
print(age30)
print(oldest)        

"""
파이썬 기초 + 셋


파이썬 데이터 타입
 : 리스트, 튜플, 딕셔너리, 셋, 배열

"""
import random
# SET
# 리스트와 달리 순어없이 중복엉ㅅ이 사용
# 순서가 없다라는 말은 입력한 순서대로 저장되지 않는다는 말
# 데이터를 변경할 수 없지만 데이터를 제거하고 샏ㄷ데이터 추가할 수 있다.
# set은 {}로 작성된다.

# SET 사용하는 경우
# 중복제거가 필요한 경우 사용
# 그룹 구성할 때 사용(집합)
"""
# SET 생성
set1 = {"사과", "배", "참외"}
print(set1)

set2 = set("member")
print(set2)

set3 = set("장영죽이가 죽을 먹었다. 근데 장영죽이가 죽을 먹다가 체했다.")
print(set3)

set4 = set(("장영실이", "수도원옷을", "입었다"))
print(set4)

#print(set4[0]) 인덱스를 사용하여 set 데이터 접근 불가

for s in set4 :
    print(s)

print("장영주가" in set4) #set 내부에 지정데이터가 있는지 확인

set4.add("김진연은")
print(set4)

set5 ={ "안경을 쓰고있다.","그래서", "겨울에는 장님이된다."}
set4.update(set5)
print(set4)
list1 = ["장영주는", "화가많다"]
set4.update(list1)
print(set4)

#set 데이터 삭제하기
#1. remove로 삭제할 경우 : 삭제할 데이터 없는 경우 오류발생
set4.remove("그래서")
print(set4)
#2. discard로 삭제할 경우 : discard는 삭제 데이터가 없으면 오류 no
set4.discard("장영주는")
print(set4)
#3. pop으로 삭제할 경우 : 마지막 데이터를 추출 삭제, 마지막 데이터를 추출하여 밖으로 빼고 set에서는 삭제
a = set4.pop()
print(set4)
print(a)
#4. clear로 삭제할 경우 :
set4.clear() #set을 비움
del set4 # set을 완전 삭제

#집합
장영주팀 = {"김기원", "김민서", "김민정", "최윤도", "정다현", "임성민", "이지현", "이종빈"}
김지연팀 = {"윤재영", "이정수", "윤종찬", "변수정", "최윤도", "이지현", "전계림", "연하남친"}

#차집합
a = 장영주팀 - 김지연팀
print(a)
#합집합
b = 장영주팀 | 김지연팀
print(b)
#교집합
c= 김지연팀 & 장영주팀
print(c)
#합집합에서 교집합 빼기
d= 김지연팀^장영주팀
print(d)

a = 장영주팀.difference(김지연팀) # 차집합
#   장영주팀.difference_update(김지연팀) # 차집합 - 장영주팀의 데이터가 변경됨
b = 장영주팀.intersection(김지연팀) # 교집합
#   장영주팀.intersection_update(김지연팀) # 교집합 - 장영주팀의 데이터가 변경됨
c = 장영주팀.symmetric_difference(김지연팀) # 합집합
#   장영주팀.symmetric_difference_update(김지연팀) # 합집합 - 장영주팀의 데이터가 변경됨
"""

이정수팀장 = {"김기원","최윤동","장영주","이종빈", "정다현","김유신","한석봉","윤재영"}
이지현팀장 = {"김지연","윤재영","윤종찬","변수정","김유신","한석봉","이순신"}

#이정수 팀원들 중에 스파이 찾기

스파이 = 이정수팀장.intersection(이지현팀장)
#       이정수팀장 & 이지현팀장
print("스파이 : {0}".format(스파이)) 

#순수 이정수팀장에세 충성하는 팀원
충신 = 이정수팀장-이지현팀장
#      이정수팀장.difference(이지현팀장)
print("이정수에게 충성맹세한 자 : {0}".format(충신))

전계림추종자 = {"장영주","윤재영","김지연","이종빈"}

#이지현팀장만 바라보는 사람들
이바사 = 이지현팀장 - 이정수팀장
이바사 = 이바사 - 전계림추종자
print("완전한 이지현 사람들 : {0}".format(이바사, len(이바사)))

# 문제 1
# Extract 10 data withou duplication in the following random range(1~50)
# 중복없이 10개의 데이터를 랜덤으로 만드세요

#내가 푼거
data = set() 
while True:
    data.add(random.randint(1,50))
    if len(data)==10: break
data = sorted(data)
print(data)

#쌤이푼거
num ={random.randint(1,50)}
while 10!=len(num):
    num.add(random.randint(1,50))
print(num)


# 문제2. 회원가입을 하는데 이름이 중복되지 않게 회원가입될 수 있도록 만들기
member = [["김춘추", "01012345678","남"],["김지연","01023478928","남"],["이순신","01025866545","남"],
["하지원", "01045566852","여"],["전계림", "01032220205","남"],["전지현", "01026557322","여"],
["윤재순", "01025885666","여"],["이지현", "01012344321","남"],["이요원", "01056664555","여"]]

# print("========= 회원가입 ==========")
# name = input("이름 : ")
# tel = input("연락처 : ")
# gender = input("성별 : ")
# member.append([name,tel,gender])  
# print(member)       

# 내가 푼거
while True:
    print("========= 회원가입 ==========")
    name = input("이름 : ")
    tel = input("연락처 : ")
    gender = input("성별 : ")
    for i in member:
        for k in i:
         if name == k:
             name =""
    if name =="":
        print("중복되는 이름입니다. 다시 입력해주세요")
    else:
     member.append([name,tel,gender])  
     break
print(member)

# 쌤이 푼거
# hint b=[1,2,3,3,2,3,4] a = set[b]
names = []
for x in member:
    names.append(x[0]) #member 이름만 가져오기
tempSet = set(names)
print("========= 회원가입 ==========")
name = input("이름 : ")

# 크기로 중복여부 확인하는 법
# a= len(set)
# set.add(name)
# if a != len(set): 

#print(tempSet)
setName = {name}
while setName.issubset(tempSet) : #name이 tempSet안에 있나 없나로 중복
    print("이름중복입니다. 다시입력하세요")
    name = input("이름 : ")
tel = input("연락처 : ")
gender = input("성별 : ")
member.append([name,tel,gender])  
print(member)     
"""
 issuperset() : b가 a에 모두 있나?
  : a.issuperset(b) 
 issubset() : A가 B에 포함되어 있나?
  : A.issubset(B) 
"""
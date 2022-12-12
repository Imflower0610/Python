"""
파이썬 기초 + 셋


파이썬 데이터 타입
 : 리스트, 튜플, 딕셔너리, 셋, 배열

"""

# SET
# 리스트와 달리 순어없이 중복엉ㅅ이 사용
# 순서가 없다라는 말은 입력한 순서대로 저장되지 않는다는 말
# 데이터를 변경할 수 없지만 데이터를 제거하고 샏ㄷ데이터 추가할 수 있다.
# set은 {}로 작성된다.

# SET 사용하는 경우
# 중복제거가 필요한 경우 사용
# 그룹 구성할 때 사용(집합)

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
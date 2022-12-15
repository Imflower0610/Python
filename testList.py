"""
파이썬 기초 + 리스트


파이썬 데이터 타입
 : 리스트, 튜플, 딕셔너리, 셋, 배열

"""


x=9
print("output : " +str(x))
print("output : {0}".format(x))

a=3.14
print("float : {0}".format(a))
print("float : {0:.1f}".format(a)) # 소수점 1자리 출력 

print(type(a))

name="김민정"
print("이름 : {0:s}".format(name))
print("이름 : "+name)
memo="을 이정수가 때렸다."

result = name + memo
print(result)
res_len = len(result)
print(res_len)

temp1=result.split()
print(temp1)
temp2 = result.split(" ",1) #,뒤에는 몇번 나눌 건지 횟수를 나타냄
print(temp2)

print(" {0}".format(",".join(temp1)))
#join은 문자열배열을 합치기 "%".join(배열) 하면 각배열의 요소 사이사이에 %가 붙은상태로 합쳐진다.
"""이것도 주석으로 사용하기도 함"""

num = int(input("숫자를 입력하세요 : ")) #input은 입력함수이다. 결과는 문자열로 반환한다. => int로 감싸줘서 정수로 반환되게 한다.
print(type(num))

# 정수타입 변환 int()
# 실수타입 변환 float()
# 문자열 타입 변환 str()

"""문제1. 국어, 수학, 영어 세과목 점수 받아서 평균 구하여 출력하기"""
kor = int(input("국어점수를 입력하세요 : "))
mat = int(input("수학점수를 입력하세요 : "))
eng = int(input("영어점수를 입력하세요 : "))
total =kor+mat+eng
print("평균점수 : " + str(total/3)) # 문자랑 숫자 같이 나와야하니까
"""
파이썬 기초 + 튜플


파이썬 데이터 타입
 : 리스트, 튜플, 딕셔너리, 셋, 배열

"""
import random

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

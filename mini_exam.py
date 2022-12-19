# txt 문서에 다음과 같은 형태로 데이터 20개 작성하기
# 번호 이름 연락처 이메일 성별 주소(동,읍,면까지만 입력)
# 위 txt 파일을 읽어와서 딕셔너리에 저장하기
# 이메일의 도메인 몇개고 무엇무엇ㅇ있는지 출력
# 성별이 여자이면서 대전중구에 사는 사람 모두 출력

# naver.com 사용하는 사람들이 사는 도시이름만 출력하기
def findNaverUser(file):
    city =[]
    for i in file:
        if "naver" in file[i]["이메일"]:
            city.append(file[i]["주소(동,읍,면까지만 입력)"])
    print("Naver를 사용하는 사람들이 사는 도시 : {0}".format(city))

# 성별로 찾는 함수
def findSex(file):
    sex = input("성별을 입력하세요 :")
    city = input("사는 구를 입력하세요(예: 대전중구) : ")
    for i in file:
        if file[i]["성별"] == sex and city in file[i]['주소(동,읍,면까지만 입력)']:
            print(file[i])
    
# 중복제거하고 출력하는 함수
def removeDuplication(email):
    domain = []
    emailList =[]
    # domainCnt = [a for a in range(len(domain))]
    for num in email:
        for i in num:
            emailList.append(i)
            if i not in domain:
                domain.append(i)
   
    # for d in range(len(domain)):
    #    domainCnt[d] = len(emailList.count(d))
  
    for n in domain:
        print("도메인 종류 : {0} : {1} 개 ".format(n,emailList.count(n)))
    
    
    

# 이메일에서 도메인 분리하는 함수
def selectDomain(file):
    email = [file[num]["이메일"] for num in file]
    domain = []
    for num in email:
        domain.append((num.split("@"))[1:])
    removeDuplication(domain)  
   

# 읽어서 딕셔너리에 저장함수
def saveFile(file):
    info = ["번호", "이름", "연락처", "이메일","성별","주소(동,읍,면까지만 입력)"]
    dictFile = dict()
    for f in range(len(file)):
        dictFile[f+1]= dict(zip(info,file[f]))
    for k in dictFile:
        print("{0}".format(dictFile[k]))
    selectDomain(dictFile)
    findNaverUser(dictFile)
    findSex(dictFile)

# 파일읽기 함수
def readFile():
    file=[]
    with open("c:/test/member.txt","r",encoding="utf-8") as f:
        file = f.readlines()
    for i in range(len(file)):
        file[i] = file[i][:len(file[i])-1] 
        file[i] = file[i].split(" ")
    print(file)
    saveFile(file)
readFile()





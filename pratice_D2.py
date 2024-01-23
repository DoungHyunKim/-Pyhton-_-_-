# 사전 
# 3번 키 -> 유재석 / 100번 키 -> 김태호
cabinet = {3:"유재석", 100:"김태호"}
print(cabinet[3])     # 출력 : 유재석
print(cabinet[100])   # 출력 : 김태호

print(cabinet.get(3)) # 출력 : 유재석
#print(cabinet[5])     # 출력 : 5번 키는 할당 x 따라서 오류.
print(cabinet.get(5))  # 출력 : 5번 키는 할당 x None으로 출력
print(cabinet.get(5,"사용가능"))  # 출력 : 5번 키는 할당 x 사용가능으로 출력

print(3 in cabinet)  # 3이라는 키가 할당되었냐? True
print(5 in cabinet)  # 5이라는 키가 할당되었냐? False

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])     # 출력 : 유재석

# new 손님
print(cabinet)
cabinet["A-3"] = "김종국"  # 만일 사용중이면 업데이트 유->김종국
cabinet["C-20"] = "조세호"  # 만일 사용중이면 업데이트
print(cabinet)

# 손님이 떠남.
del cabinet["A-3"]
print(cabinet)

# 총 사용중인 열쇠에 대해 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# 둘다 출력
print(cabinet.items())

# 목욕탕 영업종료
cabinet.clear()
print(cabinet)


# 튜플 / 리스트와 다르게 변경 x / 속도는 리스트보다 빠름

# 돈까스 집
menu =("돈까스", "치돈")
print(menu[0])
print(menu[1])

# name = "김종국"
# age = 20
# bonny = "코딩"
# print(name,age,hobby)

(name, age, hobby) = ("김종국" , 20 ,"코딩")
print(name, age, hobby)

# 세트 (set) : 집합 , 중북x, 순서 x
my_set ={1,2,3,3,3}
print(my_set)   # 출력 1,2,3 만 중복 x

java = {"유재석","김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합을 출력 (자바+파이썬 둘다 할 수 있는 사람)
print(java&python)
print(java.intersection(python))

# 합집합 (둘 중에 하나만 해도 채용)
print(java | python)
print(java.union(python))

# 차집합 (자바 할 수 있지만 파이썬은 할 줄 모르는 개발자)
print(java-python)
print(java.difference(python))

# 파이썬을 교육받아 할 줄 암
python.add("김태호")   # 파이썬 개발자에 김태호 추가
print(python)

# 자바를 까먹음
java.remove("김태호")
print(java)

# 자료구조의 변경
menu ={"커피", "우유", "쥬스"}
print(menu, type(menu))    # class = set

menu = list(menu)
print(menu, type(menu))     # class = list

menu = tuple(menu)
print(menu, type(menu))     # class = tuple

menu =set(menu)
print(menu,type(menu))      # class = set

# if 
# 날씨에 따른 행동강령
# weather = input("오늘 날씨는 어때요? ")  # 사용자의 입력을 기다림.
# if weather =="비" or weather=="눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지" :
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요.")

# temp = int(input("기온은 어때요? "))  # input은 문자 -> 정수형태로 받기위해 int
# if 30 <= temp:
#     print("너무 더워요, 나가지 마세요.")
# elif 10<= temp and temp <30 :   # 둘다 모두 성립할 때
#     print("괜찮은 날씨에요.")
# elif 0 <= temp<10 :
#     print("외투를 챙기세요.")
# else :
#     print("너무 추워요. 나가지 마세요.")

# for 반복문
# print("대기번호 : 1") ...

for waiting_no in range(1,6):  #1,2,3,4,5
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이어맨", "토르", "아이엠 그루트"]
for customer in starbucks :
    print("{0}, 커피가 준비되었습니다.".format(customer))

# while 반복문
# 5번 불렀는 데 안오면 버림
    
    customer = "토르"
    index = 5
    while index >=1 :
        print("{0}, 커피가 준비되었습니다. {1}번 남았어요.".format(customer, index))
        index -= 1
        if index == 0 :
            print("커피는 폐기처분되었습니다.")

# customer = "토르"
# index = 1
# while True:
#      print("{0}, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
#      index +=1
     # 무한루프  컨트롤 c

# customer ="토르"
# person ="Unknown"
# while person != customer :
#      print("{0}, 커피가 준비되었습니다. ".format(customer))
#      person = input("이름이 어떻게 되세요? ")
     

# continue & break

# 책을 읽게 할 것임.
absent = [2,5]  # 결석한 학생 2번과 5번
no_book = [7] # 책을 깜빡했음.
for student in range(1,11): # 1부터 10번까지 열명의 학생이 있음
    if student in absent:
        continue
    if student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break
    print("{0}, 책을 읽어봐".format(student))

# 한줄로 끝내는 for문
# 출석번호 1 2 3 4, 앞에 100을 붙임 -> 101 102 103 104
student = [1,2,3,4,5]
student = [i+100 for i in student]
print(student)

# 학생들 이름을 길이로 변환
student=["Iron man","Thor","I am groot"]
student = [len(i) for i in student]
print(student)

# 학생 이름을 대문자로 변환
student=["Iron man","Thor","I am groot"]
student = [i.upper() for i in student]
print(student)

# 함수
# def open_account():
#     print("새로운 계좌가 생성되었습니다.")  # 함수는 정의 호출하기 전까지 실행이 안됨
# open_account()  # 호출을 해줘야됨. <<<< 해야 보임 이제

# def deposit(balance,money):   # 입금 (잔액,입금할금액)
#     print("입금이 완료되었습니다. 잔액은 {0}원입니다. ".format(balance +money))
#     return balance+ money

# def withdraw(balance,money):   # 입금 (잔액,입금할금액)
#     if balance >= money: # 잔액이 출금보다 많으면
#     print("출금이 완료되었습니다. 잔액은 {0}원입니다. ".format(balance - money))
#     return balance -  money

# else:
# print("출금이 완료되지 않았습니다. 잔액은 {0}원입니다.".format(balance))
# retrun balance

# def withdraw_night(balance,money): # 저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance -money - commission


# balance = 0 # 잔액
# balance =deposit(balance, 1000)
# balance =withdraw(balance, 2000)
# commission, balance = withdraw_night(balance=,500)
# print(balance)

# 기본값
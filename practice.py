# 숫자 자료형 
print(5) 
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

# 문자형 자료
print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*9)

# boolean 자료형  참 or 거짓
print( 5> 10)     # 결과값 false
print( 5< 10)     # 결과값 true
print(True)       # 결과값 true
print(False)      # 결과값 false
print(not True)   # 결과값 false
print(not (5>10)) # 결과값 true

# 변수 
# 반려동물을 소개해주세요.

# print("우리집 강아지의 이름은 연탄이에요.")
# print("연탄이는 4살이며, 산책을 아주 좋아해요.")
# print("연탄이는 어른일까요? True")

# 변수 선언할 때, 문자는 ""안에 선언 숫자형은 그냥
name ="연탄이"
animal = "강아지"
age = 4
hobby = "산책"
is_adult = age >=3
# 정수형을 문자열로 만들어주는 str 따라서 출력할때
# age를 str로 감싸주어야한다. boolean도 포함.
print("우리집" + animal +"의 이름은 "+ name +"이에요.")
# 변수는 중간에 선언하면 마지막거를 따른다.
hobby = "공놀이"
# print(name + "는 "+ str(age) +"살이며, "+ hobby +"을 아주 좋아해요.")
# +대신 ,를 쓰면 str 쓸 필요없고 띄워쓰기가 포함이다.
print(name , "는 ", str(age) ,"살이며, ", hobby ,"을 아주 좋아해요.")
print(name +"는 어른일까요?"+ str(is_adult))


#연산자
print(1+1)
print(2**3)  # 2^3 =8
print(5%3)   #나머지 2
print(5//3)  #5를 3으로 나눴을 때 몫  = 1
print(1==1)   # True
print(1 !=3)  # True
print(not(1!=3)) # False
print((3>0)and( 3<5))  # True
print((3>0)&(3<5))     # True

print((3>0)or( 3>5))  # True  false  // or는 하나만 맞아도
print((3>0)|( 3>5))   # True  false  // or는 하나만 맞아도

#간단한 수식
number = 2+3 *4     # 14
print(number)
number = number +2  # 16
print(number)
number +=2          # 18
print(number)
number *=2          # 36
print(number)
number /=2          # 18
print(number)
number -=2          # 16
print(number)

number %=2          # 0
print(number)

# 숫자처리함수
print(abs(-5))   # 절대값
print(pow(4,2))  # 4^2
print(max(5,12)) # 최대값 반환
print(min(5,12)) # 최솟값
print(round(3.14)) # 반올림

from math import*
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(16))   #제곱근 4출력

# 랜덤함수
from random import*
print(random()) # 0.0 ~ 1.0  미만의 임의값 생성.
print(random() *10) # 0.0 ~ 10.0 미만의 임의값 생성
print(int(random()*10)) # 0 ~ 10미만의 임의값 생성
print(int(random()*10)+1) # 1~10이하의 임의 값 생성

#로또 1~49
print(int(random()*45)+1) # 1~45이하의 임의 값 생성

print(randrange(1,46)) # 1~45이하의 임의의값 생성
print(randint(1,45)) # 1부터45 이하의 임의의 값 생성

# 문자열
sentence = '나는 소년입니다.'
print(sentence)
sentence2 ="파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고 
파이썬은 쉬워요
"""
#""" """줄바꿈
print(sentence3)

# 슬라이싱 = 필요한 정보만 짤라서 쓰는 것. 
jumin = "980821-1234567"
print("성별 : " + jumin[7])  # 왼쪽에서 오른쪽으로 0부터 시작
print("년 : " + jumin[0:2])  # 0 부터 2직전까지 0,1 값
print("월 : " + jumin[2:4])  # 2,3 값
print("일 : " +jumin[4:6])   # 4,5 값
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지.
print("뒤 7자리 : " +jumin[7:])  # 7부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) #맨뒤에서 7번째부터 끝까지

# 문자열 처리함수
python = "Python is Amazing"
print(python.lower()) # lower 소문자처리
print(python.upper()) # lower 대문자처리
print(python[0].isupper()) # python 첫번째 글자가 대문자냐
print(len(python)) # 공백 포함 몇자냐
print(python.replace("Python","Java")) # reaplace 특정문자를 다른걸로 바꿔줌

index = python.index("n") # 첫번째 n만 찾아줌
print(index)
index = python.index("n",index +1) # 두번째 n만 찾아줌
print(index)

print(python.find("java")) # 찾는 글자가 없으면 -1 출력
#print(python.index("java")) # 찾는 글자가 없으면 오류 출력
print(python.count("n")) # n이 총 몇번 등장하는지 

# 문자열 포맷
print("a"+"b")
print("a","b")

# 방법 1
print("나는 %d살입니다." % 20)  # %d는 정수값만 입력
print("나는 %s을 좋아해요." % "파이썬") # %s 문자열
print("Apple은  %c로 시작해요" % "A")  # %c 한글자만 받겠다.
# %s 는 다 출력할 수 있다. 
print("나는 %s색과 %s색을 좋아해요" %("파란", "빨간"))

#방법 2 
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20,color="빨간"))

#방법 4 (v3.6 이상)
age = 20
color ="빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")

# 탈출문자 
# \n =줄바꿈
# \" \' : 문장내에서 따옴표
# \\ : 문장내에서 하나의 \로 바뀜.
# \r : 커서를 맨 앞으로 이동
# \b : 백스페이스 역할 (한글자 삭제)
# \t : 탭
print("백문이 불여일견 \n백견이 불여일타")

# 저는 "나도 코딩"입니다.
# print("저는 "나도코딩"입니다.")  << 오류
# print('저는 "나도코딩입니다".')  << 오류는 안나지만 여태 ""써옴
print("저는 \"나도코딩\"입니다.")
print("C:\\Users\\user\\Desktop\\PythonWorkspace>")
print("Red Apple \rPine")
print("Redd\bApple")   
print("Red\tApple")         

#리스트 - 순서를 따지는 객체의 집합
#지하철 칸별로 10명 20명 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는지?
print(subway.index("조세호"))    # 1번째 0,1,2

# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")    #append를 하면 맨 뒤에 타게됨.
print(subway)

# 정형돈씨를 유재석 / 조세호 사이에 태워봄.
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())   # 누구를 뺄지 ?  맨뒤인 하하
print(subway)         # 따라서 하하를 뺀 나머지4명만 출력

# 같은 이름의 사람이 몇 명 있는지 확인.
subway.append("유재석")   # append 맨뒤 유재석 탑승
print(subway)
print(subway.count("유재석")) # 유재석 이름을 가진 사람이 몇명인지

# 정렬도 가능
num_list = [5,2,4,3,1]
num_list.sort()    # 작은~큰 순서대로 정렬
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용
mix_list =["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)
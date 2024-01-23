'''
퀴즈 1) 변수를 이용하여 다음 문장을 출력하시오.
변수명 : station
변수값 : 사당, 신도림, 인천공항 순서대로 입력
출력 문장 : xx행 열차가 들어오고 있습니다.
'''

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")

'''
퀴즈 2) 당신은 최근에 코딩 스터티 모임을 새로 만들었습니다.
월 4회 스터디를 하는 데 3번은 온라인으로 하고 1번은 오프라인으로
하기로 했다.

조건 1 : 랜덤으로 날짜를 뽑아야 함.
조건 2 : 월별 날짜는 다름을 감안하여 최소 일수인 28이내로 정함.
조건 3 : 매월 1~3일은 스터디 준비를 해야 하므로 제외.

출력문 에제)
오프라인 스터디 모임 날짜는 매월 x 일로 선정되었습니다.
'''

from random import*
study = randint(4,28) # 1부터45 이하의 임의의 값 생성
print("오프라인 스터디 모임 날짜는 매월 "+str(study)+"일로 선정되었습니다.")
# study는 숫자형임으로 ++를 쓸 경우에 str를 써서 문자형으로 바꿔줘야함.
# print("오프라인 스+디 모임 날짜는 매월",study,"일로 선정되었습니다.")

'''
퀴즈 3) 사이트 별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
ex) http://naver.com
조건 1 : http:// 부분은 제외 => naver.com
조건 2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
조건 3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e'갯수
        + "!"로 구성
출력문 예제) 생성된 비밀번호 : nav51!
'''
# site = "http://naver.com"
# print(site[7:10] + str(len(site[8:13])) +str(site.count("e"))+"!")
# 퀴즈 3에 대한 나의 문제점 
# 내가 푼 위의 문제가 중간 len의 길이가 무조건 5로 맞춰짐.
# 문자열에서 숫자형으로 바꿀 때 str 까먹음. 
url = "http://youtube.com"
my_str = url.replace("http://", "")
# print(my_str)
my_str = my_str[:my_str.index(".")] 
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) +"!"
print("{0}의 비밀번호는 {1}입니다.".format(url,password))

'''
퀴즈 4) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
댓글 작성자들 주엥 추첨을 통해 1명은 치킨, 3명은 커피쿠폰을 받게 됩니다.
추첨 프로그램을 작성하시오.

조건 1 : 편의상 댓글은 20명이 작성하였고, 아이디는 1~20이라고 가정
조건 2 : 댓글 내용과 상관없이 무작위로 차첨하되 중복 불가
조건 3 : random 모듈의 shuffle과 sample을 활용

(출력 예제)
--- 당첨자 발표 ---
치킨 당첨자 : 1 
커피 당첨자 : [2,3,4]

(활용 예제)
from random import
lst= [1,2,3,4,5]
print(lst)
shuffle(lst)
print(lst)
print(sample(lst,1))
'''
from random import *
lst= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lst)
print("---당첨자 발표---"+"\n치킨당점자 : " + str(sample(lst,1))+ "\n커피당첨자 : "+ str(sample(lst,3)))

from random import *
users = range(1,21) # 1 부터 20까지 숫자를 생성
# print(type(users))  # 타입이 range
users =list(users)  # 타입을 range -> list로 변환
# print(list(users))  # 타입이 list
shuffle(users)  # 20명을 섞어줌
winners = sample(users,4)
print("--- 당첨자 발표 ---")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("--- 축하합니다. ---")

'''
퀴즈 5) 당신은 cocoa 서비스를 이용하는 택시 기사님입니다.
50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오.
조건 1 : 승객별 운행 소요 시간은 5~50분 사이의 난수로 정해집니다.
조건 2 : 당신은 소요 시간 5~15분 사이의 승객만 매칭해야 됩니다.

(출력문 예제)
[0] 1번째 손님 (소요시간 : 15분)
[ ] 2번째 손님 (소요시간 : 50분)
[0] 3번째 손님 (소요시간 : 5분)
...
[ ] 50번째 손님 (소요시간 : 16분)

총 탑승 승객 : 2분
'''

for cocoa_yes in range(1,51):  #1,2,3,4,5
    print("{0}번째 손님 (소요시간 :( )분".format(cocoa_yes))

from random import *
cnt = 0 # 총 탑승 승객 수
for i in range(1,51):  # 1~50 이라는 수 (승객)
    time = randrange(5,51)  #5~50분 사이 소요시간
    if 5<= time <=15:    # 5분~ 15분 이내의 손님, 탐승 승객수 증가 처리.
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else :   # 매칭 실패한 경우
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i,time))

print("총 탑승 승객 {0}분".format(cnt))
























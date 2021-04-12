#모듈
# import time
# print(list(time.localtime())) #localtime의 값을 list로 변환
# print(time.localtime().tm_year,'년', end=' ')
# print(time.localtime().tm_mon, '월', sep='')
# print(time.localtime().tm_mday,'일')
# print(time.localtime().tm_hour,'시')
# print(time.localtime().tm_min,'분')

# import datetime
# from datetime import datetime
# now = datetime.now()
# print(now)
# print(now.strftime('%y-%n-%d %H:%M:%S'))

#sleep함수 : 프로그램 실행 속도를 제어
# import time
# print('시작')
# time.sleep(3) #3초간 멈춤
# print('3초지남')

#timer 만들기

# from time import sleep
# sec = int(input('몇초?'))
# print('타이머 시작')
# for x in range(1,sec+1):
#     sleep(1)
#     print(x, '초')
# print('타이머 종료')

#난수모듈. 랜덤

# import random
# pa = input('플레이어 A 이름 입력')
# pb = input('플레이어 B 이름 입력')
#
# awin=0
# bwin=0
# while True:
#     a = random.randint(1,6) #1~6 사이 랜덤한 숫자를 a로
#     b = random.randint(1,6)
#     print('pa:',a,'pb:',b)
#
#     if a>b:
#         print(pa,'승리')
#     elif b>a:
#         print(pb,'승리')
#     else:
#         print('비겼습니다.')


#sample() / 로또번호추첨기
# import random
# print(random.sample(range(1,46), 6))

# #choice() : 고르기
# import random
# print(random.choice(['가위','바위','보']))
#
# #shuffle() : 섞기
# data=['나비','나비','벌','벌','꽃','꽃']
# random.shuffle(data)
# print(data)

# #거북잉
# import turtle
# turtle.shape('turtle')
# turtle.color('red')
# for x in range(4): #4번 돌아라
#     turtle.forward(100)
#     turtle.right(90)
# turtle.done()




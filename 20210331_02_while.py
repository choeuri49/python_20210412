#반복문:while
#조건이 참일 동안 실행. 무한반복. (for는 범위 내에서 실행)
# while True:
#     print('python')

# 1부터 10까지 출력
# a=0
# while True:
#     a += 1 #1씩 증가. a = a + 1.  # a에 1을 더해서 a에 다시 저장
#     if a > 10: break #a가 10보다 크면 멈추도록
#     print(a)

# 1부터 10까지 출력
# a=0
# while a<10:
#     a += 1 #1씩 증가. a = a + 1.  # a에 1을 더해서 a에 다시 저장
#     print(a)


#실습) 1~10까지 합을 while문으로 출력

# s=0 #합계를 누적할 변수
# a=0 #증가하는 변수
# while True:
#     a += 1 #a=a+1
#     if a>10: break #a가 10보다 크면 브레이크
#     s += a #s=s+a
# print(s)


#a가 증가하면서 누적합계를 구하고 그 합계가 2000이 넘으면 종료한다
# s=0 #합계누적변수
# a=0 #증가 변수
# while True:
#     a += 1 #a를 1씩 증가
#     s += a
#     if s>2000:
#         print(a,s)
#         break

#2)
# s=0
# a=0
# while s<2000: #s가 2000보다 작으면 계속 진행
#     a += 1
#     s += a
# print(a, s)


#사용자가 입력한 수를 누적하다가 만약 사용자가 0을 입력하면 반복문 종료 후 누적합계를 출력
# s=0
# a=0
# while True: #반복하고 싶은 것이 무엇인지 안에 적기
#     a=int(input('더할값은?')) #이것을 반복할 것
#     if a == 0: break #사용자가 0을 입력하면 종료.
#     s += a  # s에 사용자가 입력한 값이 계속 누적됨.
# print(s)

#위의 것을 브레이크를 쓰지 않고 표현
s=0
a=1
while a != 0:
    a=int(input('더할값은?'))
    s += a
print(s)

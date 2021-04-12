#연습문제
#1)별찍기1
# for x in range(1,7): #range : 정수의 리스트를 만들어낸다.
#     print('★' * x)

#2)별찍기2
# for x in range(6, 0, -1): #증가값은 -1
#     print('★' * x)

#3)별찍기3




#실습2) 구구단을 출력하는 프로그램 만들기
# dan = int(input('단수는?'))
# for x in range(1,10): #in 뒤에 반복할 범위 지정.
#     print('%d * %d = %d' %(dan, x, dan*x))

#2~9단까지 출력
# for x in range(1,10):
#     for y in range(1,10): #x가 1일때 이 문장을 9번 반복하라. y가 1씩 9까지 증가
#         print(x,y)


#실습3) 3의 배수 출력
#last=int(input('마지막 숫자 입력하세요.'))
# for x in range(0, last+1, 3):
#     print(x * 3,end=' ')

# for x in range(0, last+1):
#     if x%3 == 0:
#         print(x)


#실습4) 숫자 두 개와 기호를 입력받아 계산기 프로그램 만들기. 단 사용자가 q를 입력하면 계산기 프로그램 종료
#1회 말고 이것을 계속 반복해서 받고 싶다
#1) 두 수와 기호를 입력받는다.
#2) 기호에 따라 계산
#3) 계속 진행 여부 입력
#1)
# while True:
#     a=int(input('첫번째 숫자'))
#     b=int(input('두번째 숫자'))
#     sign=input('기호')
#     if sign == '+':
#         print(a + b)
#     elif sign == '-':
#         print(a - b)
#     elif sign == '*':
#         print(a * b)
#     elif sign == '/':
#         print(a / b)
#     else:
#         print('잘못된 기호')
#
#     if input('종료(y)?') == 'y': break


#2)
# while True:
#     a=int(input('첫번째 숫자'))
#     if a == 'q': break
#     a=int(a)
#     b=int(input('두번째 숫자'))
#     # 원하는 기호가 입력될 때까지 계속 입력
#     while True:
#         sign=input('기호')
#         if sign in ['+','-','*','/']:
#             break
#
#     if sign == '+':
#         print(a + b)
#     elif sign == '-':
#         print(a - b)
#     elif sign == '*':
#         print(a * b)
#     elif sign == '/':
#         print(a / b)
#     else:
#         print('잘못된 기호')


#실습5) 반학생들 점수가 딕셔너리로 저장되어 있을 때 90점 이상인 학생만 출력

# dicA = {1:94, 2:87, 3:91, 4:75, 5:92}
# print(dicA.keys()) #키만 가져옴
# print(dicA.values()) #값만 가져옴
# print(dicA.items()) #둘다 가져옴 #튜플()을 리스트[]로 묶어놓음
#
# for no,score in dicA.items(): #튜플이 no,score 로 들어감. 1번학생은 no로, 94점은 score로. 5번 반복.언패킹 기능
#     if score >= 90:
#         print(no, '번')


#실습6) 판매수량 입력받아 히스토그램을 그리는 프로그램 만들기
#1)사원의 판매수량 입력
#2)반복문으로 히스토그램 그리기
#데이터구조 : {'홍길동':10,'이순신':15,'김순희':5,'이철수':7} #딕셔너리
data = ['홍길동','이순신','김순희','이철수']
qty = {} #판매수량을 저장할 딕셔너리
for name in data:
    qty[name] = int(input(name + '?'))

print(qty)

for name, saleqty in qty.items(): #튜플이 name, saleqty 로 각각 들어감. 언패킹
    print(name, '*' * saleqty)


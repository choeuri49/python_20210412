# #조건문
# a=-1
# if a>0: #a가 0보다 크다면
#     print('양수')
#     print(a)
# else: #아니라면
#     print('음수')
#     print(a)
#
# # if와 else는 줄을 맞춰야 함
#
# print('프로그램 종료')

#실습) 회원등급 출력
#a가 90보다 크면 good, 아니면 try를 출력
# a=int(input('점수는?'))
# if a>90:
#     print('good')
# else:
#     print('try')


#실습)비밀번호 체크
#비밀번호가 일치하면 '문이 열립니다.'
#일치하지 않으면 '다시 확인하세요.'
# pw='1234' #기존 등록된 비밀번호
# inpw = input('비밀번호를 입력하세요.')
# if pw==inpw: #오른쪽은 문자. 문자인지 숫자인지 잘 구별해야.
#     print('문이 열립니다.')
# else:
#     print('다시 확인하세요.')


#어떤 수가 짝수이면 '짝수'라고 출력하고, 홀수이면 '홀수'라고 출력
# a=int(input('입력하세요'))
# if a==0: #a가 0이라면
#     print('짝수도 홀수도 아닙니다.')
# elif a%2==0: #elif: if 아닌데 만약에 ~하다면
#     print('짝수')
# else:
#     print('홀수')

#실습) 90점 이상 A, 89~80 B, 79~70 C, 69~60 D, 59~ F
# a=int(input('점수 입력하세요.'))
# if a>=90:
#     print('A')
# elif a>=80:
#     print('B')
# elif a>=70:
#     print('C')
# elif a>=60:
#     print('D')
# else:
#     print('F')


#실습) 몸무게와 키를 입력받아서 비만여부 출력
# weight=60
# height=165
# normal=(height-100)*0.9
# print('정상체중은', normal)
# if weight < normal*0.95:
#     print('미달')
# elif weight <= normal*1.05:
#     print('정상')
# else:
#     print('비만')


#내가 풀어본거
# a=input('이름')
# b=int(input('신장'))
# c=int(input('몸무게'))
# if 0.95*((b-100)*0.9) <= c < 1.05*((b-100)*0.9):
#     print(a,'정상')
# elif 0.95*((b-100)*0.9) < c:
#     print(a,'비만')
# else:
#     print(a,'마름')

#실습)계산기
# 두 수와 기호를 입력받아 사칙연산(+,-,*,/)를 출력
# 30 + 20 = 50

# a= int(input('첫번째 수'))
# b= input('기호')
# c= int(input('두번째 수'))
#
# if b == '+' :
#     print(a+c)
# elif b == '-' :
#     print(a-c)
# elif b == '*' :
#     print(a*c)
# elif b == '/' :
#     print(a/c)


#2)
#data. 결과값은 스트링. 문자열. 문자열은 스플릿이라는 메소드가 기본적 제공됨
# data=input('계산식은?').split() #입력할 때 공백을 기준으로 분리. 입력할 때 띄워써야 분리됨
# print(data)
# a=int(data[0])
# b=int(data[2])
# sign=data[1]
# if sign=='+':
#     print('%d + %d = %d'%(a,b,a+b))
# elif sign == '-':
#     print('%d - %d = %d'%(a,b,a-b))
# elif sign == '*':
#     print('%d * %d = %d'%(a,b,a*b))
# elif sign == '/':
#     print('%d / %d = %d'%(a,b,a/b))
# else:
#     print('잘못된 기호')


#3) 3번째 방법
import os
#print(os.listdir())
# data = input('계산식은?')
# #eval 함수: if문 없이 편리하게 계산 가능하나 사용 권장하지 않음. 보안 매우 취약
# print(eval(data))

#실습)두 수를 입력받아서 큰 수를 화면에 출력
# a = int(input('첫번째 수를 입력하세요.'))
# b = int(input('두번째 수를 입력하세요.'))
# if a>b:
#     print('큰 수는',a,'입니다')
# elif b>a:
#     print('큰 수는',b,'입니다')
# else:
#     print('두 수는 같습니다.')


#실습) 계산기 포스 만들기
# pay = int(input('받은 금액'))
# amount = int(input('물품 가격'))
# if pay>amount:
#     print('거스름돈:',pay-amount)
# elif amount>pay:
#     print(amount-pay,'원이 부족합니다.')
# else:
#     print('계산 완료!')

#논리연산자
# a=10; b=20
# print(a>0 and b>0) #true+true=true
# print(a>0 and b<0) #true+false=false
# print(a>0 or b<0) # or 는 둘 중 하나만 참이어도 참
# print(not(a>0)) #not 연산자 : 참을 거짓으로, 거짓을 참으로 만듬

# a=10; b=20
# if a==0 or b==0:
#     print('0이 아닌 수를 입력하세요.')
# elif a>0 and b>0:
#     print('둘다 양수')
# elif a>0 or b>0:
#     print('둘 중 하나는 음수입니다')
# else:
#     print('두 수는 음수입니다')


#실습) 음식 선택하면 가야할 코너를 알려주는 프로그램 작성하기
# price = ({'1':['자장면',5000], '2':['짬뽕',6000], '3':['설렁탕',7000],
#           '4':['비빔밥',8000], '5':['피자',9000], '6':['스파게티',10000]}) #딕셔너리 / 줄 길다고 그냥 엔터치면 안됨. 괄호로 묶어줘야함.
# print('-'*22)
# print('[국제식당]오늘의 메뉴')
# print('-'*22)
# print(' 1.자장면\n 2.짬뽕\n 3.설렁탕\n 4.비빔밥\n 5.피자\n 6.스파게티')
# print('-'*22)
# a = input('음식 번호를 입력하세요.')
# print(price[a][0], '선택') #입력한 a가 딕셔너리에서 가져오는 키가 되는 것
# print(price[a][1], '원')
# if a in['1','2']: #in: 포함 여부
#     print('중식 코너로 가세요.')
# elif a in['3','4']:
#     print('한식 코너로 가세요.')
# elif a in['5','6']:
#     print('양식 코너로 가세요.')
# else:
#     print('잘못 입력하셨습니다. 다시 입력해주세요.')

#2) if문 쓰면 유지보수가 힘듬. 최대한 안쓰도록 만들어보기
price = ({'1':['자장면',5000,'중식'], '2':['짬뽕',6000,'중식'], '3':['설렁탕',7000,'한식'],
          '4':['비빔밥',8000,'한식'], '5':['피자',9000,'양식'], '6':['스파게티',10000,'양식']}) #딕셔너리 / 줄 길다고 그냥 엔터치면 안됨. 괄호로 묶어줘야함.
print('-'*22)
print('[국제식당]오늘의 메뉴')
print('-'*22)
print(' 1.자장면\n 2.짬뽕\n 3.설렁탕\n 4.비빔밥\n 5.피자\n 6.스파게티')
print('-'*22)
a = input('음식 번호를 입력하세요.')
menukey = price.keys()
print(menukey)
if a in menukey: #만약 입력한 a가 메뉴키에 속해 있다면
    print(price[a][0], '선택') #입력한 a가 딕셔너리에서 가져오는 키가 되는 것
    print(price[a][1], '원')
    print(price[a][2], '코너로 가세요.')
else: #입력한 a가 메뉴키에 속해 있지 않다면
    print('다시 입력해 주세요.')

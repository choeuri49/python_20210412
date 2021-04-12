#사용자에게 입력받기
#a=input('이름은?')
#print('입력한 값은',a)

#실습)나이를 입력받아 화면에 출력
#입력한 값은 문자취급
#age=input('나이는?')
#print('당신의 나이는', age, '입니다.')

#실습)날씨를 입력받아 화면에 출력
#예)오늘의 날씨는 맑음
#txt='오늘의 날씨는'
#w=input('날씨:')
#print(txt, w, sep='*')

#help(print)
#help : 함수 도움말 출력

#사용자가 입력한 값에 100을 더해서 출력
#a=input('숫자는?')
#a=int(a) #int는 a를 정수로 변환해서 반환해주는 함수
#a=float(a) #a를 실수로 변환해서 반환해주는 함수
#print(a+100)

#실습) 두 수를 입력받아 사칙연산 프로그램 만들기
#1번 방법
#a=int(input('첫번째 수는?'))
#b=int(input('두번째 수는?'))
#print('%d + %d = %d'%(a,b,a+b))
#print('%d - %d = %d'%(a,b,a-b))
#print('%d * %d = %d'%(a,b,a*b))
#print('%d / %d = %d'%(a,b,a/b))
#print('두 수를 더한 값은', a+b, '입니다.')

#2)
#data = input('두 수는?').split()
#a= int(data.split()[0]) #split : 두 수를 분리. '30' '20'으로
#b= int(data.split()[1])
#print(a,'+', b, '=', a+b)

#a,b = map(int,data) #map이란 data의 각값을 int함수를 각각 적용한 후 a,b에 대입한 것
#print(a,'+', b, '=', a+b)

#실습 : 반지름 입력받아 원의 넓이 구하기
#r=int(input('반지름의 길이는?'))
#print('원의 넓이는', r*r*3.14)

#반복문:for문
# data=[5,25,34,42,57] #list
# for x in data: #반복문for, 변수x, in, 반복하고 싶은 것(data)
#     print('python', x) #list의 범위만큼 수행됨(5개) . list의 인덱스가 x에 하나씩 대입됨.

# data=['길막이','야통이','삼색이']
# for x in data: #list의 내용을 한개씩 x에 넣음
#     # print(data[0])  # data에 있는 0번 인덱스를 출력
#     print(x)
#
# for x in [0,1,2]:
#     print(data[x])


#실습)0~9까지 출력
# data=[0,1,2,3,4,5,6,7,8,9]
# for x in data:
#     print(x)

#range : 정수를 생성하는 함수. (start값이 들어가고, 그다음 stop(10이라면 10 불포함한 9까지), ~개씩 건너뛰고 싶다)
# print(list(range(0,101,3)))
# print(list(range(101)))
# print(list(range(10,20)))

#range를 이용해 0~9까지 출력
# for x in range(0,10,2): #0부터 9까지 수 중에 짝수만 출력
#     print(x)

#1~10의 합계를 구하기
#1부터 10까지 출력
# s=0 #합계를 저장할 변수
# for x in range(1,11):
#     s = x+s
#     print(s) #합계 반복 출력
# print(s) #반복문에서 빠져나와서 총합계만 출력

# s=0 #합계를 저장할 변수
# for x in range(1,11):
#     s += x #s = s+x라는 뜻
# print(s) #반복문에서 빠져나와서 총합계만 출력


#실습) 사용자에게 숫자를 입력받아 1부터 그 수까지 더하기
# s=0 #s 정의
# lastsu = int(input('마지막 숫자는?'))
# for x in range(1,lastsu+1): #in : ~의 범위 안에
#     s += x  #s에 x를 더해서 다시 s로 집어넣겠다는 복합연산자
# print(s)


#실습) 1부터 100까지의 합이 2000이 넘을 때의 수를 출력
# s=0
# for x in range(1,101):
#     s += x #s에다 x를 더해 저장
#     if s>2000:
#         break #반복문을 종료할 때 사용하는 키워드
#
# print('x=', x,'s=', s)


#실습) 바보라는 글자가 발견되면 강퇴시키기
# data=['안녕','반가워','방가','바보','오늘만나']
# bad = ['바보','멍청이'] #나쁜말 리스트
# for x in data:
#     print(x)
#     if x in bad: #bad에 in(포함)되어있다면
#         print('강퇴')
#         break
#     else: #for문의 else : if문의 else와 조금 다름. for문을 끝까지 정상수행했다면 나오는 결과를 뜻함(정상수행 : break문을 실행하지 않았을 때)
#         print('바른말 사용')



# for x in data:
#     print(x)
#     if x == '바보':
#         print('강퇴')
#         break
#     elif x == '멍청이':


#continue 키워드 : 계속 진행 이라는 뜻
#continue 사용하지 않고 짝수만 골라내기
# data=[3,4,6,8,7,10]
# for x in data:
#     if x %2 == 0:
#         print(x)

# data=[3,4,6,8,7,10]
# for x in data:
#     if x %2 == 1:continue
#     print(x)

#set: 중복데이터 허용 불가. 키가 없는 딕셔너리

#실습) 어떤 학생의 점수리스트가 주어졌을 때 모든 점수가 60점이 넘으면 합격하는 프로그램을 작성하시오
#data=[65,45,95,55,70]
# data=input('점수는?').split() #통짜로 입력된 점수들을 split으로 분리
# print(data)
# data = map(int, data) #map: 각각에 int 값을 적용하라는 뜻?
# for x in data: #for x in data를 반복한다
#     print(x)
#     if x < 60:
#         print('불합격')
#         break
# else: #불합격이 한번도 수행되지 않았다면
#     print('합격')



#점수의 합계가 300점이 넘으면 합격하는 프로그램 작성
s=0
data=[65,45,95,55,80]
for x in data:
    s += x #s에 x를 더해서 누적
    if s >= 300:
        print('합격')
        break #0~2인덱스까지 합계 300이 넘었다면 그 이상은 계산할 필요 없으므로 break
else:
    print('불합격')


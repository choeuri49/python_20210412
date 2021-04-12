#내장함수
# data=[5,8,4,6]
# print(sum(data)) #sum에 데이터를 넘김. 합계 내줌

#사용자 함수로 sum을 구현해보자.
#매개변수:리스트, 반환값:합계를 반환하라 라고 함수를 정의

# def mysum(d): #def: 정의한다 라는 뜻. mysum: 내가 만들 함수 이름 안에 매개변수는 이름 아무렇게나 지어도 됨
#     s=0
#     for x in d: #d가 반복하면서 s에 더해지길 바람
#         s += x
#     #print(s)
#     return s
#
# data=[5,18,4,6]
# r = mysum(data) #data의 변수를 d로 넘김
#
# print('리턴값:', r)


#max함수, min함수
# data=[5,18,4,6]
# m = max(data) #data에서 가장 큰 값을 가져다 m에 저장
# print('가장큰값:', m)
# mi = min(data)
# print('가장작은값:', mi)
#
# data=[5,18,4,6]
# mx = data[0] #일단 0번 인덱스가 가장 큰 값이라고 가정
# for x in data:
#     if x > mx: #x가 mx보다 크다면
#         mx = x #mx에 x값을 넣는다
# print(mx)


#위에 것을 함수로 만들고 싶다면
# def mymax(data):
#     mx = data[0]
#     for x in data:
#         if x > mx:
#             mx = x
#     return mx #이 함수의 목적은 print가 아님. 함수를 여러 곳에 쓰려면 결합도를 낮게 만들어야 함. 그래서 return 사용.
#
# #전역변수
# data2=[5,18,4,6]
# print('가장큰값:', mymax(data2))
#
# data=[78,8,5,16]
# print('가장큰값:', mymax(data)) #함수를 만들면 복붙해서 편하게 쓸 수 있음


#가장 작은 값 min값을 구하는 함수 만들기

# def mymin(mindata):
#     mi = mindata[0] #첫번째 값을 가장 작다고 가정
#     for x in mindata:
#         if x < mi:
#             mi = x #mi값에 x를 넣음
#     return mi #작은 값 나오면 함수 종료
#
# data=[5,18,4,6]
# result = mymin(data)
# print('가장 작은 값:', mymin(data))


#ord() 함수 / 아스키 코드를 알려주는 함수
#한글은 유니코드체계
# print(ord('A') ,len('A'), 'A'.encode(), len('A'.encode()))
# print(ord('가') ,len('가'), '가'.encode(), len('가'.encode()))
# print(chr(44032)) #가=44032


#실습) 두 수를 입력받아 사칙연산을 하는 함수
#매개변수 : 두 수
#반환값 : 두 수를 사칙연산 한 결과
# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a-b
#
# def cal(a,b):
#     return a+b, a-b #튜플로 변환
#
# print('더하기:', add(10,20))
# print('빼기:', sub(10,20))
# print('계산:', cal(10,20)[0], cal(10,20)[1])


#실습3) 월급 구하기
#연봉, 시급, 초과근무시간을 매개변수로 받아 월급을 계산하고 반환하는 함수
#월급 계산이 목적인 함수
#월급=연봉 / 12 + 시급*초과근무시간

def salary(yearS,timeS,overtime):
    return yearS / 12 + timeS * overtime

yearS = 1000000000
timeS = 50000
overtime = 20
print('월급은',salary(yearS,timeS,overtime))

#딕셔너리
#데이터 주고받는 형태
# data={'a':10,'b':20,'c':30,'d':40} #20을 가져오고 싶으면 b를 넣고 싶다
# print(data['b']) #딕셔너리는 인덱스순서 없음. b를 가져와야
#print(data['a':'b']) <-불가. 딕셔너리는 순서가 없으므로. 딕셔너리는 원하는 데이터를 끄집어낼 수 있는 장점이 있다.
#리스트: 대괄호로 여러개 넣음.
#튜플: 데이터를 절대 변경하지 않아야 할 때 튜플에 저장

#
# data={'홍길동':20, '이순신':45}
# print(data['홍길동'], '살')

# data={'홍길동':[20,165.5],'이순신':45}
# print(data['홍길동'][1]) #딕셔너리에서 '홍길동' 키를 부르고, 결과값에서 어떤 인덱스를 취할것인지 [1] 표시
#
# data={'홍길동':{'나이':20, '키':165.5},'이순신':{'나이':45, '키':176}}
# print(data['홍길동']['나이']) #data 라는 곳에서 홍길동 딕셔너리에서 '나이'라는 키를 입력해서 홍길동의 나이를 가져온다
#
# data={1:['홍길동',20,165.5], 2:['이순신', 45,176]}
# print(data[2][0])
#
# #딕셔너리에 데이터 추가
# data={}
# data['홍길동']=20 #홍길동은 20살이다 라는 정보 추가하고 싶을 때
# data['이순신']=[45,176] #2가지 이상 데이터를 넣고 싶으면 리스트로 감싸서 표시
# print(data)


#실습) 좋아하는 컴퓨터 언어를 입력받아 딕셔너리에 저장
#{'backend':'java', 'frontend':'html5'}
# lang={} #딕셔너리
# back = input('backend 언어는?')
# lang['backend'] = back
# print(lang)
#
# front = input('frontend 언어는?')
# lang['frontend'] = front
# print(lang)

#lang. #딕셔너리에 어떤 기능을 주고 싶다면 .찍고 메소드

#오늘의 영화 순위
data={1:'고질라',2:'귀멸의칼날',3:'더박스'}
print(data.keys()) #.key : 키(1,2,3)만 가져오고 싶다
print(list(data.keys()))
print(list(data.values())[0]) #딕셔너리는 인덱스 쓸 수 없지만, 안에서 list로 만들어주면 인덱스를 쓸 수 있다




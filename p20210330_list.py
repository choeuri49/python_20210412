#리스트
#리스트란? 연속적인 메모리의 할당
#일반적인 변수에는 하나의 값밖에 저장 못함
#리스트는 여러 개의 데이터를 한 개의 변수에 저장할 수 있음
#data=[10,20,30,40,50] #여러 개의 데이터를 저장하기 위한 대괄호
#print(data[0])#여러 개 데이터 중 특정 데이터를 꺼내오고 싶으면 인덱스로
#print(data[1:3])#20,30을 가져오고 싶다면. 3에서 stop(3포함x)이므로 30을 가져오고 싶으면 인덱스 2 다음 3
#print(data[:-1])
#data[1] = 200 #데이터 중 1번 인덱스를 200으로 하고 싶다
#data[5] = 200 #index 초과
#오른쪽은 변수 = 왼쪽은 값
#data.append(200) #append : 추가. data에 200을 추가하고 싶다.
#print(data)
#data.clear()

#data = ['홍길동', 20, 165.8]
#print(data[0], data[1], data[2])
data=[['홍길동', 20, 165.8],['이순신', 40, 170.5]]
#이순신만 꺼내오려면?
print(data[1][0])
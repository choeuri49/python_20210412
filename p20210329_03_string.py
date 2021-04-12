#문자열 다루기
txt = 'python is easy!'
print(txt[1]) #인덱스가 1번인 것을 가져와라
print(txt[-1]) #마지막 데이터
print(txt[-2]) #마지막에서 두번째 데이터
print(txt[7:9]) # start indes : stop index . 7에서 8까지 출력하고 싶다면
print(txt[0:2])
print(txt[:2]) #0번은 생략 가능
print(txt[10:14])
print(txt[10:-1]) #데이터 가져올 때 마지막 데이터를 빼고 싶다면
print(txt[-5:-1])
print(txt[-5:]) #마지막 번호까지 가져오고 싶을 때, 마지막 번호는 생략가능

#실습1
s = 'my house'
print(s[3:])

#실습2
txt= "012345678901234567890123456"
print(txt[:10])
print(txt[10:20])
print(txt[20:])
#class : 객체를 만들기 위한 틀
class Car: #클래스 이름은 대문자로 하는 것이 약속
    #속성 : 필드라고 부른다. 차의 특징
    name='이오닉스5'
    color='실버'
    pw=False #파워 꺼져있는 상태
    #기능:메소드
    def power(self):
        pw = not Car.pw

#Car라는 객체 만들어짐. 객체는 사람1, 사람2와 같다. 틀을 만들고 그 안에서 독립적인 공간을 만든 것
c1=Car()
print(c1.name)
c1.power()

c2=Car()
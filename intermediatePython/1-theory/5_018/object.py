# 클래스 만들기
# 클래스 : class, 속성, 기능으로 구성

# 객체는 클래스의 생성자를 호출한다

class Car:

    def __init__(self, col, len):
        self.color = col
        self.length = len

    def doStop(self):
        print('STOP')

    def doStart(self):
        print('START!!!')

    def printCarInfo(self):
        print(f'self.color : {self.color}')
        print(f'self.length : {self.length}')



car1 = Car('red', 200) # 객체를 생성하여 변수(레퍼런스 변수) 에 담음
car2 = Car('blue', 300)

car1.printCarInfo()
car2.printCarInfo()
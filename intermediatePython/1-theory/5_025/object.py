# 다중상속 : 2개 이상의 클래스를 상속받는 것
class Car01:

    def drive(self):
        print('drive() method called!!')

class Car02:

    def turbo(self):
        print('turbo() method called!!')

class Car03:

    def fly(self):
        print('fly() method called!!')

class Car(Car01, Car02, Car03):
    def __init__(self):
        pass

myCar = Car()
myCar.drive()
myCar.turbo()
myCar.fly()

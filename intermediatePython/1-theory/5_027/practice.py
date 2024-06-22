# 추상클래스 : 상위 클래스에서 하위 클래스에 메서드 구현을 강요
from abc import ABCMeta
from abc import abstractclassmethod

class Airplane():

    @abstractclassmethod
    def flight(self):
        pass
    def forward(self):
        print('전진 !!')
    def backward(self):
        print('후진 !!')

class Airliner(Airplane):
    def __init__(self, c):
        self.color = c

    def flight(self):
        print('시속 400km/h 비행중!')

class flighterPlane(Airplane):
    def __init__(self, c):
        self.color = c
    def flight(self):
        print('시속 700km/h 비행중!')
    
ai = Airliner('red')
ai.flight()
ai.forward()
ai.backward()


# 오버라이딩 : 하위 클래스에서 상위 클래스의 메서드를 재정의(override) 한다.
class Robot:

    def __init__(self, c, h, w):
        self.color = c
        self.height = h
        self.weight = w

    def fire(self):
        print('미사일 발사!')

    def printRobotInfo(self):
        print(f'self.color : {self.color}')
        print(f'self.height : {self.height}')
        print(f'self.weight : {self.weight}')

class NewRobot(Robot):
    def __init__(self, c, h, w):
        super().__init__(c, h, w)

    # fire() 재정의
    def fire(self):
        print('레이저 발사로 업그레이드!')

myRobot = NewRobot('red', 200, 300)
myRobot.printRobotInfo()
myRobot.fire()

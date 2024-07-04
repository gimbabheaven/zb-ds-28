# 객체와 메모리
# 변수는 객체의 메모리 주소를 저장하고 이를 이용해서 객체를 참조한다.

class Robot:
    def __init__(self, color, height, weight):
        self.color = color
        self.height = height
        self.weight = weight

    def printRobotInfo(self):
        print(f'color : {self.color}')
        print(f'height : {self.height}')
        print(f'weight : {self.weight}')
        print('-'*30)

# 변수가 있어야 객체에 접근 가능함
# 변수 rb1은 Robot 객체의 주소값 가지고 있음
rb1 = Robot('red', 200, 80) 
#rb1.printRobotInfo()


rb2 = Robot('blue', 300, 120)

rb3 = rb1 # rb1가 가지고 있는 객체의 '메모리 주소'를 나타냄, 결과적으로 rb3, rb1은 같은 객체를 나타낸다.

rb1.printRobotInfo()
rb2.printRobotInfo()
rb3.printRobotInfo()

rb1.color = 'gray'
rb1.height = 250
rb1.weight = 100
print('\n')

rb1.printRobotInfo()
rb2.printRobotInfo()
rb3.printRobotInfo()







# 얕은 복사 : 객체 주소를 복사하는 것으로, 객체 자체가 복사되지 않는다. 다른 변수가 동일 객체를 가리킴
# 깊은 복사 : 객체 자체를 복사하는 것으로, 또 하나의 객체가 만들어진다. 객체 자체가 하나 더 생성됨

class TemCls:
    def __init__(self, n, s):
        self.number = n
        self.str = s

    def printClasInfo(self):
        print(f'self.number  :  {self.number}')
        print(f'self.str  :  {self.str}')

# 얕은 복사
# tc1 = TemCls(10, 'Hello')
# tc2 = tc1

# print('*** 얕은 복사 ***')
# print('-'*30)
# tc1.printClasInfo()
# tc2.printClasInfo()
# print('-'*30)

# tc2.number = 3.14
# tc2.str = 'Bye'
# print('-'*30)
# tc1.printClasInfo()
# tc2.printClasInfo()
# print('-'*30)


# 깊은 복사
import copy

tc1 = TemCls(10, 'Hello')
tc2 = copy.copy(tc1) #얕은 복사
tc3 = copy.deepcopy(tc1) #깊은 복사

tc1.printClasInfo()
tc2.printClasInfo()
tc3.printClasInfo()

tc2.number = 3.14
tc2.str = 'Bye'

print('\n')
tc1.printClasInfo()
tc2.printClasInfo()
tc3.printClasInfo()
import copy

class TemCls:
    def __init__(self, n, s, lst):
        self.number = n
        self.str = s
        self.lst = lst

    def printClasInfo(self):
        print(f'self.number  :  {self.number}')
        print(f'self.str     :  {self.str}')
        print(f'self.lst     :  {self.lst}')

# 원본 객체 생성
tc1 = TemCls(10, 'Hello', [1, 2, 3])

# 얕은 복사
tc2 = copy.copy(tc1)

# 깊은 복사
tc3 = copy.deepcopy(tc1)

# 원본 및 복사본 출력
print('*** 초기 상태 ***')
print('원본 (tc1):')
tc1.printClasInfo()
print('얕은 복사본 (tc2):')
tc2.printClasInfo()
print('깊은 복사본 (tc3):')
tc3.printClasInfo()

# 얕은 복사본 수정
tc2.number = 3.14
tc2.str = 'Bye'
tc2.lst.append(4)

print('\n*** 얕은 복사본 수정 후 ***')
print('원본 (tc1):')
tc1.printClasInfo()
print('얕은 복사본 (tc2):')
tc2.printClasInfo()
print('깊은 복사본 (tc3):')
tc3.printClasInfo()

class Calculator:

    def __init__(self, n1, n2):
        print(f'[Calculator] __init__() called!!')
        self.num1 = n1
        self.num2 = n2

cal = Calculator(10, 20)

print(f'cal num1 : {cal.num1}')
print(f'cal num2 : {cal.num2}')


## __init()__ : 속성을 초기화

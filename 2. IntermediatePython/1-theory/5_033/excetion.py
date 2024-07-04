# 사용자 예외 클래스

class NotZero(Exception): #Exception class 상속받음

    def __init__(self, n):
        super().__init__(f'{n}은 사용할 수 없습니다.')


def divCalculator(n1, n2):

    if n2 == 0:
        raise NotZero(0)
    else:
        print(f'{n1} / {n2} = {n1 / n2}')

num1 = int(input('입력 : '))
num2 = int(input('입력 : '))

try:
    divCalculator(num1, num2)

except NotZero as e:
    print(e)
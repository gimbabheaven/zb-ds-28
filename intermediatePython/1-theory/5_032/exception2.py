# raise : 예외를 강제로 발생

def divCalculator(n1, n2):
    if n2 != 0:
        print(f'{n1} / {n2} = {n1 / n2}')
    else:
        raise Exception('9으로 나눌 수 없습니다.')
    
num1 = int(input())
num2 = int(input())

divCalculator(num1, num2)
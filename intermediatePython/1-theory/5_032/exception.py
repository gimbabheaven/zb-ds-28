# exception 클래스 : 예외 담당 클래스

num1 = int(input('number1 : '))
num2 = int(input('number2 : '))

try:
    print(f'num1 / nnm2 = {num1 / num2}')
except Exception as e:
    print('0으로 나눌 수 없습니다.')
    print(f'exception : {e}')
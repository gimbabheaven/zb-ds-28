# 인수와 매개변수

def great(customer1, customer2):
    print('{}님, {}님 안녕하세요?'.format(customer1, customer2))

great('홍길동', '박찬호')

# 인수와 매개변수는 일치해야 한다 > 아닐 시 missing error 발생

def calculator(n1, n2):
    print(f'{n1} + {n2} = {n1 + n2}')

calculator(10, 12)

# 매개변수 개수가 정해지지 않은 경우 *를 이용한다.
# *를 이용한 매개변수 타입은 <class 'tuple'> => 매개변수 갯수가 정해지지 않았으므로

def printNumber(*numbers):
    for number in numbers:
        print(number, end="")
    print('-'*20)

printNumber()
printNumber(10)
printNumber(10, 20)
printNumber(10, 20, 30)
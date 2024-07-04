# lambda
# lambda 키워드를 이용하면 함수 선언을 보다 간단하게 할 수 있다.
'''
def calculator(n1, n2):
    return n1 + n2

returnValue = calculator(10, 20)
print(f'returnValue : {returnValue}')
'''

calculator = lambda n1, n2 : n1+n2

returnValue = calculator(10, 20)
print(f'returnValue : {returnValue}')
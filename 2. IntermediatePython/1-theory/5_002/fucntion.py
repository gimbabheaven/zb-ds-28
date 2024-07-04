# 함수 선언
'''
def : definition
키워드 : 함수명()
실행부는 들여쓰기 후 작성
'''


def calFuc():
    n1 = int(input('n1 입력 : '))
    n2 = int(input('n2 입력 : '))
    
    print(f'n1 + n2 = {n1 + n2}')
    print(f'n1 - n2 = {n1 - n2}')
    print(f'n1 * n2 = {n1 * n2}')
    print(f'n1 / n2 = {n1 / n2}')

calFuc()
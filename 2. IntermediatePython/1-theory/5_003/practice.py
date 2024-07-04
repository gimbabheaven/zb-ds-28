'''
구구단 출력 함수가 연쇄적으로 호출되도록 작성
'''

def guguDan2():
    print('-'*20)
    for i in range(1, 10):
        print('2 * {} = {}'.format(i, 2 * i))
    print('-'*20)
    guguDan3()

def guguDan3():
    for i in range(1, 10):
        print('3 * {} = {}'.format(i, 3 * i))
    print('-'*20)
    guguDan4()

def guguDan4():
    for i in range(1, 10):
        print('4 * {} = {}'.format(i, 4 * i))
    print('-'*20)
    guguDan5()

def guguDan5():
    for i in range(1, 10):
        print('5 * {} = {}'.format(i, 5 * i))
    print('-'*20)

guguDan2()
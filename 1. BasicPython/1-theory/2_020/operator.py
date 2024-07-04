# 논리연산자
'''
종류 : and, or, not
(1) and : A and B : A와 B모두 True인 경우
(2) or : A or B : A와 B중 어느 하나만 True인 경우
(3) not : not A : A의 상태를 부정하는 결과 나타냄
'''

print('-'*30)
print()
print('{} and {} : {}'.format(True, True, (True and True)))
print('{} and {} : {}'.format(False, True, (False and True)))
print('{} and {} : {}'.format(True, False, (True and False)))
print('{} and {} : {}'.format(False, False, (True and True)))
print('-'*30)
print()
print('{} or {} : {}'.format(True, True, (True or True)))
print('{} or {} : {}'.format(False, True, (False or True)))
print('{} or {} : {}'.format(True, False, (True or False)))
print('{} or {} : {}'.format(False, False, (True or True)))
print('-'*30)
print()
print('not {}'.format(True, (not True)))
print('not {}'.format(False, (not False)))


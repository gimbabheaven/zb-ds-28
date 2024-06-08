'''
random과 operator모듈을 사용해서 10부터 100사이의 난수 중 
십의 자리와 일의 자리가 각각 3의 배수인지 판단하는 코드
'''

import random
import operator

random = random.randint(1, 100)

#십의자리
num1 = operator.floordiv(random, 10)
rlt1 = operator.eq(operator.mod(num1, 3), 0)
#일의자리
num2 = operator.mod(random, 10)
rlt2 = operator.eq(operator.mod(num2, 3), 0)

print('랜덤 숫자 : {}\n십의 자리 : {}, 3의 배수 : {}\n일의 자리 : {}, 3의 배수 : {}'.format(random, num1, rlt1, num2, rlt2))


# 오퍼레이터 모듈
'''
모듈 : 누군가 이미 만들어놓은 훌륭한 기능
(수학 연산, 난수, 연산자...etc)

* operator 모듈
'''
import operator

num1 = 8
num2 = 3

# 산술연산자 
print('{} + {} : {}'.format(num1, num2, operator.add(num1, num2)))
print('{} - {} : {}'.format(num1, num2, operator.sub(num1, num2)))
print('{} * {} : {}'.format(num1, num2, operator.mul(num1, num2)))
print('{} / {} : {}'.format(num1, num2, operator.truediv(num1, num2))) #나눗셈
print('{} % {} : {}'.format(num1, num2, operator.mod(num1, num2))) #나머지
print('{} // {} : {}'.format(num1, num2, operator.floordiv(num1, num2))) #몫
print('{} ** {} : {}'.format(num1, num2, operator.pow(num1, num2))) #거듭제곱
print()
# 비교연산자
print('{} == {} : {}'.format(num1, num2, operator.eq(num1, num2))) 
print('{} != {} : {}'.format(num1, num2, operator.ne(num1, num2))) 
print('{} > {} : {}'.format(num1, num2, operator.gt(num1, num2))) 
print('{} >= {} : {}'.format(num1, num2, operator.ge(num1, num2))) 
print('{} < {} : {}'.format(num1, num2, operator.lt(num1, num2))) 
print('{} <= {} : {}'.format(num1, num2, operator.le(num1, num2))) 
print()

# 논리연산자
flag1 = True
flag2 = False
print('{} or {} : {}'.format(flag1, flag2, operator.or_(flag1, flag2))) 
print('{} and {} : {}'.format(flag1, flag2, operator.and_(flag1, flag2))) 
print('not {} : {}'.format(flag1, operator.not_(flag1))) 
print('not {} : {}'.format(flag2, operator.not_(flag2))) 
print()


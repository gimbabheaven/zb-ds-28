'''
백신 접종 대상자는 20세 미만 또는 65세 이상자에 한합니다.
'''
import operator

userAge = int(input('나이를 입력하세요 : '))

min = 20
max = 65

minResult = operator.lt(userAge, min)
print(f'minResult : {minResult}')
maxResult = operator.ge(userAge, max)
print(f'maxResult : {maxResult}')

result = operator.or_(minResult, maxResult) 
print('입력하신 나이는 {}세 이며, 접종 대상 여부는 {}입니다.'.format(userAge, result))
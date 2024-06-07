'''
비 올 확률을 입력하고 
비 올 확률이 55%이상이면 '우산을 챙기세요'
그렇지 않으면 '양산을 챙기세요'를 출력하는 코드
'''
import operator

rain = int(input('비 올 확률 : '))
limit = 55
result = operator.ge(rain, limit)

if result:
    print('비 올 확률 : {}%!! 우산을 챙기세요.'.format(rain))
else:
    print('비 올 확률 : {}%!! 양산을 챙기세요'.format(rain))
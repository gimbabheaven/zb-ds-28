'''
1. 최저 기온 입력
2. 최고 기온 입력
3. 일교차가 11도 이상인 경우: 일교차, 감기조심하세요
4. 일교차가 11도 미만인 경우: 일교차, 산책하기 좋은 날씨 입니다.
'''
import operator

min = int(input('최저 기온 입력 : '))
max = int(input('최고 기온 입력 : '))

limit = 11
sub = operator.sub(max, min)
result = operator.ge(sub, limit)

if result:
    print('오늘 일교차는 {}도, 감기조심하세요.'.format(sub))
else:
    print('오늘 일교차는 {}도, 산책하기 좋은 날씨 입니다.'.format(sub))

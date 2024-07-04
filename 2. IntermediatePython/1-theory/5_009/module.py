# 모듈 : 이미 만들어진 기능, 사용자는 쉽게 사용할 수 있다.
'''
내부 모듈 : 파이썬 설치 시 기본적으로 사용할 수 있는 모듈
외부 모듈 : 별도 설치 후 사용할 수 있는 모듈
사용자 모듈 : 사용자가 직접 만든 모듈
'''

import random

rNum = random.randint(1, 10) # 1 부터 10 까지의 난수
print(f'rNum : {rNum}')


rNums = random.sample(range(1, 101), 10)
print(f'rNums : {rNums}')
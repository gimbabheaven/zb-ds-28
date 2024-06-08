'''
10의 팩토리얼을 계산하는 과정에서 결과값이 50이 넘을 때의 숫자
'''

factorial = 10
limit = 1
num = 0

for i in range(1, 11):
    limit *= i

    if limit > 50:
        num = i
        break

print('cnt : {}, limit : {}'.format(num, limit))
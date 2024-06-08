# 반복문
# 1. 횟수에 의한 반복 2. 조건에 의한 반복
print('{} * {} = {}'.format(2, 1, (2 * 1)))
print('{} * {} = {}'.format(2, 1, (2 * 2)))
print('{} * {} = {}'.format(2, 1, (2 * 3)))
print('{} * {} = {}'.format(2, 1, (2 * 4)))
print('{} * {} = {}'.format(2, 1, (2 * 5)))

print()
print('-'*30)
for i in range(1, 6):
    print('{} * {} = {}'.format(2, 1, (2 * i)))

print()
print('-'*30)
players = ['박찬호', '박세리', '박지성', '김연경', '이승엽']
for player in players:
    print('{}선수 에게 메일 발송!'.format(player))
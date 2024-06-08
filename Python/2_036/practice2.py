'''
새끼 강아지 체중이 2.2kg가 넘으면 이유식 중단
한 번 이유식 시 70g증가
예상되는 이유식 날짜? 현재는 800g
'''

max = 2200
curr = 800
once = 70
num = 1

while True:
    if curr >= max:
        break

    num += 1
    curr += once
print('이유식 중단 날짜 : {}일, 현재 몸무게 : {}'.format(num, curr))
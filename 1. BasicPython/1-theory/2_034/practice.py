'''
하루에 독감으로 병원에 내방하는 환자가 50명에서 100명 사이일 때,
누적 독감 환자 수가 최초로 10,000명을 넘는 날짜를 구해보자
'''
import random

sum = 0
date = 1
flag = True

while flag:
    cnt = random.randint(50, 100)
    sum += cnt
    date += 1
    print('{} 일 째 | 오늘 환자 수 : {} | 누적 환자 수 {}'.format(date, cnt, sum))

    if sum >= 10000:
        flag = False
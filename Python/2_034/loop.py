# 무한 루프
flag = True
num = 0
sum = 0

while flag:
    num += 1
    sum += num
    print('{}까지의 합 : {}'.format(num, sum))

    if sum >= 10:
        flag = False
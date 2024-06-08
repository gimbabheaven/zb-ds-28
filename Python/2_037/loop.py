# 중첩 반복문 : 반복문 안에 또 다른 반복문 선언
# 별찍기..

for i in range (1, 10):
    for j in range (i):
        print('*', end='')
    print()

for i in range (10, 0, -1):
    for j in range(i):
        print('*', end='')
    print()
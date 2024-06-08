'''
1부터 100까지의 정수 중 3과 7의 공배수와 최소공배수를 출력
'''
min = 0

for i in range(1, 101):
    if i % 3 != 0 or i % 7 != 0:
        continue
    print(f'공배수 : {i}')

    if min == 0:
        min = i
else:
    print(f'최소 공배수 : {min}')        
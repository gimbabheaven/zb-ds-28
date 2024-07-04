# while
cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']

n = 0
while n < len(cars):
    print(cars[n])
    n +=1
print()
n=0
flag = True
while flag:
    print(cars[n])
    n += 1
    if n == len(cars):
        break

print()
studentCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

n = 0
sum = 0
avg = 0
while n < len(studentCnts):
    classNo = studentCnts[n][0]
    cnt = studentCnts[n][1]
    print(f'{classNo} 학급의 학생 수 : {cnt}명')

    sum += cnt
    n += 1

print(f'전체 학생 수 : {sum}\n평균 학생 수 : {sum / len(studentCnts)}')


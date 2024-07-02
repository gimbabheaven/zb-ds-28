cars = '그랜저', '소나타', '말리부', '카니발', '쏘렌토'

for i in range(len(cars)):
    print(cars[i])

print()

for n in cars:
    print(n)

print()
studentCnts = ((1, 19), (2, 28), (3, 37), (4, 20), (5, 30))

for i in range(len(studentCnts)):
    print(f'{studentCnts[i][0]} 학급 학생 수 : {studentCnts[i][1]}')

print()
for classNo, cnt in studentCnts:
    print(f'{classNo} 학급 학생 수 : {cnt}')
    
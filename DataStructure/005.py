cars = ['그랜저', '소나타', '말리부', '카니발', '쏘렌토']

# 인덱스 이용
for i in range(len(cars)):
    print(cars[i])

print()

# 리터러블 객체 이용
for item in cars:
    print(item)

# 리스트 내 리스트

studentsCnts = [[1, 19], [2, 20], [3, 22], [4, 18], [5, 21]]

for i in range(len(studentsCnts)):
    print('{} 학급의 학생 수 : {}'.format(studentsCnts[i][0], studentsCnts[i][1]))

print()

for classNo, cnt in studentsCnts:
    print('{} 학급의 학생 수 : {}'.format(classNo, cnt))


## 학급별 학생 수와 전체 학생 수 그리고 평균 학생 수 출력
print()
print()
print()

stdCnts = [[1, 18], [2, 19], [3, 23], [4, 21], [5, 20], [6, 22], [7, 17]]

print(len(stdCnts))
sum = 0
avg = 0

# 1. 학급별 학생 수
for cls, cnts in stdCnts:
    sum += cnts
    print('{}반의 학생 수는 {}명 입니다.'.format(cls, cnts))

avg = sum / len(stdCnts)

print('전체 학생 수 : {} 명, 평균 학생 수 : {:.2f} 명'.format(sum, avg))

student1 = '홍길동'
student2 = '박찬호'
student3 = '이용규'
student4 = '박승철'
student5 = '김지은'

# 리스트
students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']

print(students)
print(type(students))

for i in students:
    print(i)


# 튜플 : 한 번 정해진 데이터는 변경할 수 없음
students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
print(students)
print(type(students))

for i in students:
    print(i)

# 딕셔너리 : key, value
scores = {'kor' : 95, 'eng' : 80, 'mat': 100}
print(scores)
print(type(scores))

# 중복 데이터는 하나
allSales = {100, 200, 500, 200}
print(allSales)
print(type(allSales))





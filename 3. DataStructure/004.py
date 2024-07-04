students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']

print(students)

sLength = len(students) # len()
print(sLength)

# 인덱스 활용
for i in range(len(students)):
    print(students[i])

print()

# 변수 활용
for a in students:
    print(a)

print()

n = 0
while n < len(students):
    print(students[n])
    n += 1
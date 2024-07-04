students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')
print(students)
print(len(students))

for i in range(len(students)):
    print(f'{i} : {students[i]}')

print()
n = 0
while n < len(students):
    print(f'{n} : {students[n]}')
    n += 1

for student in students:
    print(f'{student}')
    
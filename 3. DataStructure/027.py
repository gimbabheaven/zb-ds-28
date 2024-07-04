students = '홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은'
print(f'1 : {students} : {type(students)}')

students = list(students)
students.sort()
print(f'2 : {students} : {type(students)}')

students = tuple(students)
print(f'3 : {students} : {type(students)}')

result = sorted(students)

print(f'4 : {students} : {type(students)}')
print(f'5 : {result} : {type(result)}')


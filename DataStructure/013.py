# remove

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은', '이용규', '강호동']
print(students)

# students.remove('이용규')
# print(students)

# 여러개 삭제시
while '이용규' in students:
    students.remove('이용규')

print(students)

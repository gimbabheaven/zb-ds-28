# 리스트 아이템 조회

students = ['박찬호', '홍길동', '이용규', '박승철', '김지은']
print(students[0])
print(students[1])
print(students[2])
print(students[3])
print(students[4])

numbers = [3.14, 20, '삼십', 40.0, 50]
print(type(numbers[0]))
print(type(numbers[1]))
print(type(numbers[2]))
print(type(numbers[3]))
print(type(numbers[4]))


people = ['김성예', '신성도', '박기준', '최승철', '황동석']

for i in range(len(people)):
    if i % 2 == 0:
        print('짝수학생 : {}'.format(people[i]))
    else:
        print('홀수학생 : {}'.format(people[i]))


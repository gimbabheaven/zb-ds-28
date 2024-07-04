# insert
students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']
print(students)

# index = 3 위치에 데이터 추가
students.insert(3, '강호동')
print(students)


numbers = [1, 3, 6, 11, 45, 54, 62, 74, 85]

inputNumber = int(input('숫자 입력 : '))
insertIdx = 0

for idx, number in enumerate(numbers):
    print(idx, number)

    if insertIdx == 0 and inputNumber < number:
        insertIdx = idx
    else:
        insertIdx = len(numbers)+1
        
numbers.insert(insertIdx, inputNumber)
print('numbers : {}'.format(numbers))
students = ('김성예', '신경도', '최승철', '황동석')

print('=== 인덱스 짝수 ===')
print()
print('0 : {}'.format(students[0]))
print('2 : {}'.format(students[2]))
print('=== 인덱스 짝수 ===')
print()
print('1 : {}'.format(students[1]))
print('3 : {}'.format(students[3]))

print()
print('for문 사용')
for i in range(len(students)):
    if i % 2 == 0:
        print('짝수 인덱스 {} : {}'.format(i, students[i]))
    else:
        print('홀수 인덱스 {} : {}'.format(i, students[i]))

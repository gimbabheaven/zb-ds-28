students = {'s1' : '홍길동',
            's2' : '박찬호',
            's3' : '이용규',
            's4' : '박승철',
            's5' : ['박세리', '박공주']}


print(students['s1'])
print(students['s2'])
print(students['s3'])
print(students['s4'])
print(students['s5'][0])
print(students['s5'][1])

print()

print(students.get('s1'))
print(students.get('s2'))
print(students.get('s3'))
print(students.get('s4'))
print(students.get('s5')[0])
print(students.get('s5')[1])
# append()

students = ['홍길동', '박찬호', '이용규', '박승철', '김지은']

print(f'students : {students}'
      )
students.append('강호동')

print(f'students : {students}')
print(f'length : {len(students)}')
print(f'last index : {len(students)-1}')


scores = [['국어', 88], 
          ['영어', 91],
          ]

print(f'scores : {scores}')
print(f'scores length : {len(scores)}')
print(f'last index : {len(scores)-1}')

scores.append(['수학', 96])
print(f'scores : {scores}')
print(f'scores length : {len(scores)}')
print(f'last index : {len(scores)-1}')

for subject, score in scores:
    print(f'{subject} : {score}')
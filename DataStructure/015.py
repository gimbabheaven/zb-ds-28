students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print(f'students : {students}')

# 오름차순
students.sort()
print(f'sort() : {students}')

# 내림차순
students.sort(reverse=True)
print(f'sort(reverse=True) : {students}')


scores = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]

scores.sort() # 오름차순 정렬

scores.pop(0) # 최저점수 제거
scores.pop(len(scores)-1) # 최고점수 제거

print(scores)


# 튜플 슬라이싱
students = ('홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은')
print(students)
print(students[2:4])
print(students[:4])
print(students[2:])
print(students[2:-2:2]) # 단계 설정도 가능함
print(students[-5:-2])

print()
print(students[slice(2, 4)])
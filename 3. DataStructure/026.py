students = '홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은'
print(type(students))
print(students)

stdList = ['홍길동', '박찬호', '이용규', '강호동']
print(f'{type(stdList)} : {stdList}')

stdList = tuple(stdList)
print(f'{type(stdList)} : {stdList}')

stdList = list(stdList)
print(f'{type(stdList)} : {stdList}')

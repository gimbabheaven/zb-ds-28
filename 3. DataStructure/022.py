students = ('홍길동', '박찬호', '이용규', '박승철', '김지은')

searchName = input('학생 이름 입력 : ')

if searchName in students:
    print(f'{searchName}은(는) 우리 반 학생입니다.')
else:
    print(f'{searchName}은(는) 명단에 없습니다.')

    


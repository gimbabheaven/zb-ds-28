students = ['홍길동', '박찬호', '이용규', '강호동', '박승철', '김지은']
print(students)

students.reverse()
print(students)


print()
print()

#암호 해독 프로그램
secret = '27156231'
secretList = []
solvedList = ''
print(f'secret : {secret}')

for cha in secret:
    secretList.append(int(cha))

print(f'secretList : {secretList}')

secretList.reverse()

print(f'reverse() : {secretList}')


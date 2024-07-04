userName = 'Hong gil dong'
userAge = 21

print(userName)
print(userAge)

print('User name : {}'.format(userName))
print('User age : {}'.format(userAge))

print('User name : {}, User age : {}'.format(userName, userAge))
print('User name : {1}, User age : {0}'.format(userName, userAge)) # 인덱스 번호 통해 순서 변경

print('나의 이름은 {0}이고, 나이는 {1}살 입니다. {0}이름은 아버님께서 지어 주셨습니다.'.format(userName, userAge, userName))


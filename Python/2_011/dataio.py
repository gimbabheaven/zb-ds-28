# 데이터 출력
userName = 'hong gil dong'
# print(userName)

userAge = 20
# print(userAge)

# print('User name : ', userName)
# print('user age : ', userAge)

#자동개행 없애기
print('3 * 6 = ', end='') #디폴트 값인 자동개행(\n)을 없애고자 할 때
print(3 * 6)


#포멧 문자열을 이용한 데이터 출력

print(f'User name : {userName}')
print(f'User age : {userAge}')
print(f'User name : {userName}, User Age : {userAge}')


#특수문자
# \t 탭, \n 개행

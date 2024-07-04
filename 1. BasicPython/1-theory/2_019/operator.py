# 문자 비교: 아스키 코드를 이용한 비교 연산
cha1 = 'A' # 65
cha2 = 'S' # 83

print('\'{}\' > \'{}\' : {}'.format(cha1, cha2, (cha1 > cha2)))
print('\'{}\' >= \'{}\' : {}'.format(cha1, cha2, (cha1 >= cha2)))
print('\'{}\' < \'{}\' : {}'.format(cha1, cha2, (cha1 < cha2)))
print('\'{}\' <= \'{}\' : {}'.format(cha1, cha2, (cha1 <= cha2)))
print('\'{}\' == \'{}\' : {}'.format(cha1, cha2, (cha1 == cha2)))
print('\'{}\' != \'{}\' : {}'.format(cha1, cha2, (cha1 != cha2)))

print()
print('-'*30)
#ord : 문자 > 아스키코드
print('\'A\' -> {}'.format(ord('A')))
print('\'S\' -> {}'.format(ord('S')))

#chr : 아스키코드 > 문자
print('65 -> {}'.format(chr(65)))
print('83 -> {}'.format(chr(83)))

print()
print('-'*30)
# 문자열 자체 비교
str1 = 'Hello'
str2 = 'hello'

print('{} == {} : {}'.format(str1, str2, (str1 == str2)))
print('{} != {} : {}'.format(str1, str2, (str1 != str2)))
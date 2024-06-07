'''
나이가 65세 이상이면 교통 요금 무료를 적용하는 프로그램
'''
age = 65

userAge = int(input('나이를 입력하세요 : '))
if userAge >= age:
    print('무료 요금 대상자 입니다.')
else:
    print('대상자가 아닙니다.')
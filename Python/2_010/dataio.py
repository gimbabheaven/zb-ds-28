# 데이터 입력
'''
input() 함수를 이용해서 입력한 데이터는 항사 문자(열) 자료형
'''

# print('키보드를 통해서 데이터를 입력하세요.')
#userInputData = input('키보드를 통해서 데이터를 입력하세요') #가이드 문구와 함께 출력

# print('입력 : ', userInputData)
# print(userInputData)
# print(type(userInputData))


# 입력 받으면서 형변환 처리

# userInputData = int(input('입력 : '))
# userInputData = bool(input('입력 : '))
# userInputData = float(input('입력 : '))

# print(userInputData)
# print(type(userInputData))


print('----------------------------------------------')

width = int(input('가로 길이 입력 : '))
height = int(input('세로 길이 입력 : '))

print(width * height)
print(width * height / 2)

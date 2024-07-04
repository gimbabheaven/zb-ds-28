'''
숫자 두 개를 입력한 후 비교 연산 결과를 출력하는 코드 작성
'''

num1 = int(input('첫 번째 숫자 입력 : '))
num2 = int(input('두 번째 숫자 입력 : '))

print('{} > {} : {}'.format(num1, num2, (num1 > num2)))
print('{} >= {} : {}'.format(num1, num2, (num1 >= num2)))
print('{} < {} : {}'.format(num1, num2, (num1 < num2)))
print('{} <= {} : {}'.format(num1, num2, (num1 <= num2)))
print('{} == {} : {}'.format(num1, num2, (num1 == num2)))
print('{} != {} : {}'.format(num1, num2, (num1 != num2)))

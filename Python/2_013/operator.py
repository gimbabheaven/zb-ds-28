
# 숫자 끼리의 덧셈
num1 = 10
num2 = 0.13

print(num1 + num2)
print('num1 + num2 = %.2f' % (num1+num2))

#문자 끼리의 덧셈
str1 = 'Good'
str2 = ' '
str3 = 'Morning'

print(str1 + str2 + str3)

#숫자와 문자의 연산 : Not Supported Operand type

# 실습 : 이번달 알바비와 카드값을 입력하고, 남은 금액이 얼마인지 출력해보자
partTimeMoney = int(input('알바비 : '))
cardMoney = int(input('카드값 : '))

result = partTimeMoney - cardMoney

print()
print('알바비 : {}'.format(partTimeMoney))
print('카드값 : {}'.format(cardMoney))
print('남는돈 : {}'.format(result))


print()
print('남는돈 : %f' % result)



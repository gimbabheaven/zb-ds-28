#   몫 연산자
num1 = 10
num2 = 3

division = num1 / num2
quotient = num1 % num2
result = divmod(num1, num2) # 한 번에 구하기

print('division : {:.2f}'.format(division))
print('quotient : {}'.format(quotient))
print('result : {}'.format(result))
print('result_div : {}, result_quo : {}'.format(result[0], result[1]))
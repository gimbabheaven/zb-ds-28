num1 = 2
num2 = 3

result = num1 ** num2
print(result)
print()
# 제곱근 구하기
# 2의 제곱근

result = 2 ** (1/2)
print('result : {:.2f}'.format(result))
print('reuslt : %.2f' % result)
print(f'result : {result:.2f}')
print()

# 2의 세제곱근
result = 2 ** (1/3)
print('result : {:.2f}'.format(result))
print('result : %.2f' % result)
print(f'result : {result:.2f}')
print()

# 2의 네제곱근
result = 2 ** (1/4)
print('result : {:.2f}'.format(result))
print('result : %.2f' % result)
print(f'result : {result:.2f}')
print()

print('-------------------------------------------------')
print()
# 제곱근 sqrt(), 거듭제곱 pow()
import math
# 2, 3, 4의 제곱근
print('2의 제곱근 : {:.2f} \n3의 제곱근 : {:.2f}\n4의 제곱근 : {:.2f} '.format(math.sqrt(2), math.sqrt(3), math.sqrt(4)))
print()

# 2, 3, 4의 거듭제곱
# N의 M제곱 : pow(N, M)
print('2의 3제곱 : %d\n3의 4제곱 : %d' % (pow(2, 3), pow(3, 4)))
print()


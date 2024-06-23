# 사용자가 입력한 숫자에 대한 소수를 구하고 이를 파일에 작성해보자

uri = '/Users/lydia/workspace/zb-ds-28/intermediatePython/text/'

def writePrimeNumber(n):
    file = open(uri + 'prime_numbers.txt', 'a')
    file.write(str(n))
    file.write('\n')
    file.close()

inputNumber = int(input('0보다 큰 정수 입력 : '))
for number in range(2, (inputNumber + 1)):
    flag = True
    for n in range(2, number):
        if number % n == 0:
            flag = False
            break
    if flag:
        writePrimeNumber(number)
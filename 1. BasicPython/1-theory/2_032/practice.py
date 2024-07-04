'''
1부터 100까지의 정수 중 
2의 배수와 3의 배수를 구분해서 출력
'''
import operator

start = 1
end = 100

while start < 101:
    if start % 2 == 0:
        print('{}은 2의 배수이다.'.format(start))
    if start % 3 == 0:
        print('{}은 3의 배수이다.'.format(start))
    start +=1
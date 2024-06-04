#1. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자

random = 13
val = random % 2


if random % 2 == 1:
    print(random, '은 홀수 입니다.')
else: 
    print(random, '은 짝수 입니다.')


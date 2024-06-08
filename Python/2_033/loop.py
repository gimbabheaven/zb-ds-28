# for vs while

# for문이 적합한 경우 : 횟수에 의한 반복


# while문이 적합한 경우 : 조건에 의한 반복
sum = 0
maxInt = 0
for i in range(1, 101):
    if i % 7 == 0 and sum <= 50:
        sum += i
        maxInt = i
    print('i : {}'.format(i))

print('7의 배수의 합이 50인 이상인 최초의 정수 : {}'.format(maxInt))

sum = 0
maxInt = 0
n = 1

while n<=100 and sum <= 50:
    n += 1
    if n % 7 == 0:
        sum += n
        maxInt = n
    print('n : {}'.format(n))

print('7의 배수의 합이 50인 이상인 최초의 정수 : {}'.format(maxInt))
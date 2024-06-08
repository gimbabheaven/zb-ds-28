# break : 실행을 중단하고 반복문을 빠져나오기
num = 0
while True:
    print('Hello ~~')
    num += 1
    if num >= 5:
        break
print('Bye ~~')


sum = 0
searchNum = 0

for i in range(100):
    sum += i

    if sum > 100:
        searchNum = i
        break
print('searchNum : {}'.format(searchNum))
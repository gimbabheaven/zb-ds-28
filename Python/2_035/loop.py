# continue : 실행을 중단하고 다음 반복 실행문으로 넘어간다.
# else : 반복문이 종료된 후 실행

cnt = 0
for i in range (100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수 입니다.'.format(i))
    cnt += 1
else:
    print('99까지의 정수 중 7의 배수는 {}개 입니다.'.format(cnt))

nums = []
n = 1
while n < 6:
    try:
        num = int(input(' numbers ? '))

    except:
        print('예외 발생')
        continue

    else: # 예외가 발생하지 않으면 실행
        if num % 2 == 0:
            nums.append(num)
            n += 1
        else:
            print('홀수 입니다. 다시 입력하세요')
        continue
print(nums)

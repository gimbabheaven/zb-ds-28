

nums = []

n = 1
while n < 6:
    try:
        num = int(input('number : '))
    except:
        print('예외 발생')
        continue

    nums.append(num)
    n += 1

print(f'nums : {nums}')
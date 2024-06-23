# 로또 번호 생성기 프로그램을 만들고 파일에 번호를 출력해보자

import random

uri = '/Users/lydia/workspace/zb-ds-28/intermediatePython/text/'

def writeNumbers(nums):
    for idx, num in enumerate(nums):
        with open(uri + 'lotto.txt', 'a') as f:
            if idx < len(nums) - 2:
                f.write(str(num) + ',')
            elif idx == len(nums) -2:
                f.write(str(num))
            elif idx == len(nums) -1:
                f.write('\n')
                f.write('Bonus : ' +str(num))
                f.write('\n')


rNums = random.sample(range(1, 46), 7)
print(f'Nums : {rNums}')

writeNumbers(rNums)


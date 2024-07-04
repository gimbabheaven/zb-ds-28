# 파일 닫기 생략
# with ~ as를 사용하면 파일 닫기(close)를 생략할 수 있다.

uri = '/Users/lydia/workspace/zb-ds-28/intermediatePython/text/'

# file = open(uri + '5_037.txt', 'a')
# file.write('python study')
# file.close()

# 자동화 ㄱㄱ

with open(uri + '5_037.txt', 'a') as f:
    f.write('\npython study!!!!')

with open(uri + '5_037.txt', 'r') as f:
    print(f.read())
    
import time

file = open('/Users/lydia/workspace/zb-ds-28/intermediatePython/text/test.txt', 'r') # 읽기모드
 
str = file.read()

print(f'str : {str}')

file.close()



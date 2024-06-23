import time

file = open('/Users/lydia/workspace/zb-ds-28/intermediatePython/text/aboutPython.txt', 'r', encoding='UTF-8') # 읽기모드
 
str = file.read()
print(f'str \n {str}')

file.close()

str = str.replace('Python', '파이썬', 2) # 대상 문자열 , 바꿀 문자열, 바꿀 갯수
print(f'str \n {str}')

file = open('/Users/lydia/workspace/zb-ds-28/intermediatePython/text/aboutPython.txt', 'w', encoding='UTF-8') # 쓰기모드
file.write(str)
file.close()



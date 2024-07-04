'''
파일 모드
w : 쓰기 전용(파일이 있으면 덮어씌움)
a : 쓰기 전용(파일이 있으면 덧붙임)
x : 쓰기 전용(파일이 있으면 에러 발생)
r : 읽기 전용(파일이 없으면 에러 발생)
'''
uri = '/Users/lydia/workspace/zb-ds-28/intermediatePython/text/'

# 'w' 파일 모드
# file = open(uri + 'hello.txt', 'w') # 현재 hello.txt 없음
# file.write('Hello python!')
# file.close()



# 'w' 파일 모드
# file = open(uri + 'hello.txt', 'a') # append 모드
# file.write('\nNice to meet you!')
# file.close()


# 'x' 파일 모드
# file = open(uri + 'hello.txt', 'x') # 파일이 존재하면 오류남
# file.write('Nice to meet you!')
# file.close()

# 'r' 파일 모드
file = open(uri + 'hello.txt', 'r') 
str = file.read()
print(str)
file.close()

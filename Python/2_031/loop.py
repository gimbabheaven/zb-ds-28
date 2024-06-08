'''
 사용자가 반복의 시작과 끝을 입력하면 1씩 증가하는 반복문
'''

start = int(input('시작 번호를 입력하세요 : '))
end = int(input('끝 번호를 입력하세요 : '))

for i in range(start, (end+1)):
    print(i)
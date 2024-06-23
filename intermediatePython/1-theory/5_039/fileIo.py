# readlnes() : 파일의 모든 데이터를 읽어서 리스트 형태로 반환

uri = '/Users/lydia/workspace/zb-ds-28/intermediatePython/text/'

""" with open(uri + 'languages.txt', 'r') as f:
    lanList = f.readlines() # 모든 것을 읽어서 리스트로 반환

print(type(lanList))
print(lanList)
 """

with open(uri + 'languages.txt', 'r') as f:
    line = f.readline()

    while line != '':
        print(f'line : {line}', end='')
        line = f.readline()
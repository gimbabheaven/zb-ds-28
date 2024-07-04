scoreDic = {}
uri = '/Users/lydia/workspace/zb-ds-28/intermediatePython/text/'

with open(uri + 'scores.txt', 'r') as f:
    line = f.readline()

    while line != '':
        tempList = line.split(':')
        scoreDic[tempList[0]] = int(tempList[1].strip('\n')) # key[0] - value[1] 선언
        line = f.readline()

print(f'scoreDic : {scoreDic}')


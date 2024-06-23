uri = '/Users/lydia/workspace/zb-ds-28/intermediatePython/text/'

scoreDic = {'kor' : 85, 'eng' : 90, 'mat' : 85, 'sci' : 79, 'his' : 82}
scoreList = [85, 90, 92, 79, 82]
# for key in scoreDic.keys():
#     with open(uri + 'scoreDic.txt', 'a') as f:
#         f.write(key + '\t:' + str(scoreDic[key]) + '\n')


with open(uri + 'scores.txt', 'a') as f:
    print(scoreList, file=f)


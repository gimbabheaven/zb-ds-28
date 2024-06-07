'''
학급 전체 학생 수 입력
한 모둠에 속하는 학생 수 입력
전체 모둠 수와 남는 학생 수 출력
'''

allStuCnt = int(input('학급 전체 학생 수 : '))
partCnt = int(input('한 모둠에 속하는 학생 수 : '))

# 전체 모둠 수, 남는 학생 수
result = divmod(allStuCnt, partCnt)

print('전체 모둠 수 : {} \n남는 학생 수 : {}'.format(result[0], result[1]))



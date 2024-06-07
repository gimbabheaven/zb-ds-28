'''
국어, 영어, 수학 점수를 입력하고 평균이 90점 이상이면 
'참 잘했어요'를 출력하는 코드
'''
import operator

korScore = int(input('국어 점수 입력 : '))
engScore = int(input('영어 점수 입력 : '))
mthScore = int(input('수학 점수 입력 : '))

limitScore = 90
totalScore = korScore + engScore + mthScore
avgScore = operator.truediv(totalScore, 3)

if operator.ge(avgScore, limitScore):
    print('참 잘했어요.')
else:
    print('아쉬워요.')
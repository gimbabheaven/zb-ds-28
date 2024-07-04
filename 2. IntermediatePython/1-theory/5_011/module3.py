from scores import *

korScore = int(input('국어 점수 입력 : '))
engScore = int(input('영어 점수 입력 : '))
matScore = int(input('수학 점수 입력 : '))

addScore(korScore)
addScore(engScore)
addScore(matScore)

print(f'점수 : {getScores()}')
print(getTotalScore())
print(getAvgScore())

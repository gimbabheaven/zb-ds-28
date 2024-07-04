korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
mthScore = int(input('수학 점수 : '))

totalScore = korScore + engScore + mthScore
avgScore = totalScore / 3

print('국어 점수 : {}, 영어 점수 : {}, 수학 점수 : {}'.format(korScore, engScore, mthScore))
print(f'평균 점수 : {avgScore:.2f}')
print('평균 점수: {:.2f}'.format(avgScore))
print('평균 점수 : %.2f' % avgScore)
'''
국어, 영어, 수학 점수를 입력하고 평균이 70점 이상이면
True를 출력하는 코드
'''
korScore = int(input('국어 점수 입력 :'))
engScore = int(input('영어 점수 입력 :'))
mthScore = int(input('수학 점수 입력 :'))

pass1 = 60
pass2 = 70

korResult = korScore >= pass1
engResult = engScore >= pass1
mthResult = mthScore >= pass1

subResult = korResult and engResult and mthResult
average = (korScore + engScore + mthScore) / 3
avgResult = average >= pass2

print('국어 : {}, 과락 여부 : {}'.format(korScore, korResult))
print('영어 : {}, 과락 여부 : {}'.format(engScore, engResult))
print('수학 : {}, 과락 여부 : {}'.format(mthScore, mthResult))
print('평균 점수 : {}\n평균 결과 : {}'.format(average, avgResult))
print()
print('최종 결과 : {}'.format(subResult and avgResult))
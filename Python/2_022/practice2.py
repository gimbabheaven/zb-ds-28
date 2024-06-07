'''
국어, 영어, 수학 점수를 입력하면 조건식을 이용해서 
과목별 결과와 전체 결과를 출력하는 코드를 작성해보자

과목별 합격점수 : 60
전체 합격 평균 : 70
'''
import operator

korScore = int(input('국어 점수 : '))
engScore = int(input('영어 점수 : '))
mthScore = int(input('수학 점수 : '))

subLimit = 60
avgLimit = 70

totalScore = korScore + engScore + mthScore
avgScore = operator.truediv(totalScore, 3)

korResult = operator.ge(korScore, subLimit)
engResult = operator.ge(engScore, subLimit)
mthResult = operator.ge(mthScore, subLimit)

subResult = korResult and engResult and mthResult
avgResult = operator.gt(avgScore, avgLimit)

finalResult = operator.and_(subResult, avgResult)
print()
print('국어 점수 : {}, 결과 : {}\n영어 점수 : {}, 결과 : {}\n수학 점수: {}, 결과{}\n\n평균 점수 : {:.2f}, 총점 : {}\n결과 : {}\n\n'
      .format(korScore, korResult, engScore, engResult, mthScore, mthResult, avgScore, totalScore, avgResult)) 
print(' !! 합격 !! ') if operator.and_(subResult, avgResult) else print(' ㅜㅜ 불합격 ㅜㅜ')

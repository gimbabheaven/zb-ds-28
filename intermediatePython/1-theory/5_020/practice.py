# 국어, 영어, 수학 점수를 입력받아 리스트에 저장하고 원본을 유지한 상태로 복사본을 만들어 
# 과목별 점수를 10% 올렸을 경우에 평균을 출력해 보자


    
scores = [int(input('국어 점수를 입력하세요 : ')),
          int(input('영어 점수를 입력하세요 : ')),
          int(input('수학 점수를 입력하세요 : '))]

print('이전 점수 : ', scores)

copyScores = scores.copy() # copy() :

for idx, score in enumerate(copyScores):
    result = score * 1.1
    copyScores[idx] = 100 if result > 100 else result

print('이후 점수 : ', copyScores)
print(f' 이전 평균 : {sum(scores)/len(scores)}')
print(f' 이후 평균 : {sum(copyScores)/len(copyScores)}')



    

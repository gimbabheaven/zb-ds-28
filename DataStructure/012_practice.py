# 최고점수, 최저점수 삭제
scores = [9.5, 8.9, 9.2, 9.8, 8.8, 9.0]
print(scores)

minScore = 0; maxScore = 0
minScoreIdx = 0; maxScoreIdx = 0

for idx, score in enumerate(scores):
    if idx == 0 or minScore > score:
        minScoreIdx = idx
        minScore = score

print(f'최저 점수 : {minScoreIdx} 번째 {minScore}')
scores.pop(minScoreIdx)

for idx, score in enumerate(scores):
    if maxScore < score:
        maxScoreIdx = idx
        maxScore = score

print(f'최고 점수 : {maxScoreIdx} 번째 {maxScore}')
scores.pop(maxScoreIdx)

print(f'최종 : {scores}')
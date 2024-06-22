import copy

playerOriginScore = [8.7, 9.1, 8.9, 9.0, 7.9, 9.5, 8.8, 8.3]
playerCopyScore = playerOriginScore.copy()

playerOriginScore.sort()
playerCopyScore.sort()

print('-'*30)
print(f'playerOriginScore : {playerOriginScore}')
print(f'playerCopyScore : {playerCopyScore}')
print('-'*30)

playerCopyScore.pop(0)
playerCopyScore.pop()

print(f'playerOriginScore : {playerOriginScore}')
print(f'playerCopySCore : {playerCopyScore}')
print('-'*30)

originTotal = round(sum(playerOriginScore), 2)
originAvg = round(originTotal / len(playerOriginScore), 2)

print(f'Original Total : {originTotal}')
print(f'Original Avg : {originAvg}')
print('-'*30)

copyTotal = round(sum(playerCopyScore), 2)
copyAvg = round(originTotal / len(playerCopyScore), 2)

print(f'Copy Totel : {copyTotal}')
print(f'Copy Avg : {copyAvg}')
print('-'*30)

print(f'originAvg - copyAvg : {originAvg - copyAvg}')
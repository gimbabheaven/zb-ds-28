import copy

scores = [9, 8, 5, 7, 6, 10]
scoresCopy = []

#scoresCopy = scores
#scoresDeepCopy = scores

# print(f'scores : {scores}')
# print(f'scoresCopy : {scoresCopy}')
# print(f'scoresDeepCopy : {scoresDeepCopy}')

print()

for s in scores:
    scoresCopy.append(s)

print(f'id(scores) : {id(scores)}')
print(f'id(scoresCopy) : {id(scoresCopy)}')
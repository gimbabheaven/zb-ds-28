minScore = 60

scores = ('국어', 58), ('영어', 77), ('수학', 89), ('과학', 99), ('국사', 50) 
print(scores)

print()
print('===과락인 경우만 출력===')
for sub, score in scores:
    if score <= 60:
        print(f'{sub} : {score}')
print()
for sub, score in scores:
    if score > 60: continue
    print(f'{sub} : {score}')
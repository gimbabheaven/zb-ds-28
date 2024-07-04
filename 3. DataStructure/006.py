# for문과 if문을 이용해서 과락 과목 출력하기

minScore = 60

scores = [
    ['국어', 58]
  , ['영어', 77]
  , ['수학', 89]
  , ['과학', 99]
  , ['국사', 50]
]
print('CASE 1')
for item in scores:
    if item[1] < minScore:
        print('과락 과목 명 : {}, 점수 : {}'.format(item[0], item[1]))
print('CASE 2')
for subject, score in scores:
    if score < minScore:
        print('과락 과목 명 : {}, 점수 : {}'.format(item[0], item[1]))
print('CASE 3')
for subject, score in scores:
    if score >= minScore: continue
    print('과락 과목 명 : {}, 점수 : {}'.format(item[0], item[1]))





scores = {'kor':88,
          'eng':55,
          'mat':85,
          'sci':57,
          'his':82}
print(scores)

del scores['his']
print(scores)

scores.pop('kor')
print(scores)
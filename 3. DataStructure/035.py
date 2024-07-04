scores = {'kor':88,
          'eng':55,
          'mat':85,
          'sci':57,
          'his':82}

# 60점 미만이면 F(재시험)

minScore = 60
result  = 'F(재시험)'

if scores['kor'] < minScore : scores['kor'] = result
if scores['eng'] < minScore : scores['koengr'] = result
if scores['mat'] < minScore : scores['mat'] = result
if scores['sci'] < minScore : scores['sci'] = result
if scores['his'] < minScore : scores['his'] = result

print(scores)
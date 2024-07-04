scores = (('1학급', 18)
          , ('2학급', 19)
          , ('3학급', 23)
          , ('4학급', 21)
          , ('5학급', 20)
          , ('6학급', 22)
          , ('7학급', 17))

minClass = ''; minScore = 0
maxClass = ''; maxScore = 0

for cls, score in scores:
    if cls == '1학급' or score < minScore:
        minScore = score
        minClass = cls
    if cls == '1학급' or score > maxScore:
        maxScore = score
        maxClass = cls

print(f'최소 학급 - {minClass} - 학생 수 {minScore} 명')
print(f'최고 학급 - {maxClass} - 학생 수 {maxScore} 명')
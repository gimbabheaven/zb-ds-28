# 다자택일 조건문
# 사용시 조건식 순서가 매우 중요함 !!! 
exampleScore = int(input('시험 성적 입력 : '))
grades = ''

if exampleScore >= 90:
    grades = 'A'
elif exampleScore >= 80:
    grades = 'B'
elif exampleScore >= 70:
    grades = 'C'
elif exampleScore >= 60:
    grades = 'D'
else:
    grades = 'F'

print('성적 : {}\t학점 : {}'.format(exampleScore, grades))
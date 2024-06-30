sports = ['농구', '축구', '야구', '마라톤', '테니스']

for i in range(len(sports)):
    print('{} : {}'.format(i, sports[i]))

print()

for idx, value in enumerate(sports):
    print('{} : {}'.format(idx, value))

print()

str = 'Hello Python'

for idx, value in enumerate(str):
    print('{} : {}'.format(idx, value))
    
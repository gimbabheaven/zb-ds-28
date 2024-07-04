sports = ['농구', '축구', '야구', '마라톤', '테니스']

favorite = input('가장 좋아하는 스포츠 입력 : ')

bestIdx = 0
for idx, value in enumerate(sports):
    if value == favorite:
        bestIdx = idx + 1

print(f'가장 좋아하는 {favorite}는 {bestIdx} 번째에 있습니다.')


my = [1, 3, 5, 6, 7]
friend = [2, 3, 5, 8, 10]
print(f'my : {my}')
print(f'friend : {friend}')

addList = my + friend
print(f'addList : {addList}')

result = []
for number in addList:
    if number not in result:
        result.append(number) # 중복되지 않은 데이터만 더하기

print(f'result : {result}')
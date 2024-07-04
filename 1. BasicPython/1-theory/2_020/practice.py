'''
백신 접종 대상자는 20세 미만 또는 65세 이상자에 한합니다.
'''
age = int(input('나이를 입력하세요 : '))

result = age < 20 or age >= 65

print('당신은 {}세이며, 백신 접종 대상자 여부는 {}입니다.'.format(age, result))
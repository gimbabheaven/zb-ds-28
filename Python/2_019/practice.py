'''
알파벳을 이용하면 아스키 코드를 출력하는 코드
'''
userInput = input('알파벳 입력 : ')
print('{} -> {}'.format(userInput, ord(userInput)))

'''
아스키 코드를 입력하면 문자를 출력하는 코드
'''
userInput2 = int(input('숫자 입력 : '))
print('{} -> {}'.format(userInput2, chr(userInput2)))
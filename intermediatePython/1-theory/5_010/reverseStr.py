# 문자열을 거꾸로 반환하는 모듈

def reverseStr(str):
    reversedString = ''
    for c in str:
        reversedString = c + reversedString

    return reversedString
# 사용자가 길이(cm)을 입력하면 mm로 환산하는 함수
def cmTomm(cm):
    
    mm = cm * 10
    return mm

cm = int(input('변환할 길이(cm)을 입력하세요 :'))
mm = cmTomm(cm)
print(f'cm = {cm}, mm = {mm}')

# 1부터 100까지의 정수 중에서 홀수인 난수를 반환하는 함수 선언
import random

def getOddRandomNumber():
    while True:
        rNum = random.randint(1, 100)
        if rNum % 2 != 0:
            break
    return rNum

print(f'returnValue = {getOddRandomNumber()}')
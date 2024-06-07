'''
자동차의 전장과 전폭을 입력하면 자동차 기계 세차 가능여부를 출력하는 코드
'''
maxLength = 5200
maxWidth = 1985

userLength = int(input('전장 길이 입력 : '))
userWidth = int(input('전폭 길이 입력 : '))

resultLength = userLength < maxLength
resultWidth = userWidth < maxWidth

if(resultLength == True):
    if(resultWidth == True):
        print("전장 : {}mm, 전폭 {}mm 으로 세차 {}합니다.".format(userLength, userWidth, '가능'))
    elif(resultWidth == False):
        print("전장 : {}mm, 전폭 {}mm 으로 세차 {}합니다.\n사유 : 전폭 길이 초과".format(userLength, userWidth, '불가능'))
elif(resultLength == False):
        if(resultWidth == False):
            print("전장 : {}mm, 전폭 {}mm 으로 세차 {}합니다.\n사유 : 전장, 전폭 길이 초과".format(userLength, userWidth, '불가능'))        
        elif(resultWidth == True):
            print("전장 : {}mm, 전폭 {}mm 으로 세차 {}합니다.\n사유 : 전장 길이 초과".format(userLength, userWidth, '불가능'))        
             

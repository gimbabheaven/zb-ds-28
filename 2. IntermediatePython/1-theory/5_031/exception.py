# finally : 예외 발생과 상관없이 항상 실행한다.

try:
    inpnutData = input(' input number ? ')
    numInt = int(inpnutData)

except:
    print('exception raise!')
    print('not number!')
else:
    if numInt % 2 == 0:
        print('even number!!')
    else:
        print('odd number!')
finally:
    print(f'InputData : {numInt}')

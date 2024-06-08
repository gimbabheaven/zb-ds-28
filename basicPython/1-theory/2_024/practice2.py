'''
소수점 첫 번째 자리에서 반올림하는 프로그램을 만들어보자
'''
floatNum = float(input('소수 입력 : '))

if floatNum - int(floatNum) >= 0.5:
    print('올림 : {}'.format(int(floatNum) + 1))
else:
    print('버림 : {}'.format(int(floatNum)))
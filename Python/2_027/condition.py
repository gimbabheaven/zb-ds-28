'''
자동차 배기량에 따라 세금을 부과한다고 할 떄,
다음 표를 보고 배기량을 입력하면 세금이 출력되는 프로그램
'''

print('-'*50)
print('배기량\t\t\t세금')
print('5000cc이상\t\t600,000')
print('5000cc미만 4000cc이상\t500,000')
print('4000cc미만 3000cc이상\t400,000')
print('3000cc미만 2000cc이상\t300,000')
print('2000cc미만 1000cc이상\t200,000')
print('1000cc미만\t\t100,000')
print('-'*50)

inputNum = int(input('자동차 배기량을 입력하세요 : '))

if inputNum >= 5000:
    print('배기량 : {}cc\n세금 : 600,000'.format(inputNum))
elif inputNum >= 4000 and inputNum < 5000:
    print('배기량 : {}cc\n세금 : 500,000'.format(inputNum))
elif inputNum >= 3000 and inputNum < 4000:
    print('배기량 : {}cc\n세금 : 400,000'.format(inputNum))
elif inputNum >= 2000 and inputNum < 3000:
    print('배기량 : {}cc\n세금 : 300,000'.format(inputNum))
elif inputNum >= 1000 and inputNum < 2000:
    print('배기량 : {}cc\n세금 : 200,000'.format(inputNum))
else:
    print('배기량 : {}cc\n세금 : 100,000'.format(inputNum))

    
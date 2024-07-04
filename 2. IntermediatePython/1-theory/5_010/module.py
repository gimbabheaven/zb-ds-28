import calculator
import lottoMachine
import reverseStr

# 계산기
calculator.add(10, 20)
calculator.sub(10, 20)
calculator.mul(10, 20)
calculator.div(10, 20)


#로또 번호 생성
result = lottoMachine.getLottoNumbers()
print(f'Lotto Numbers : {result}')


#문자열 거꾸로 출력
str = 'HELLO'
reversed = reverseStr.reverseStr(str)
print(f'reversed str : {reversed}')
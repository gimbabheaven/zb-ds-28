#변수 작명법
'''
(1) 가급적 데이터의 의미를 파악할 수 있는 명사 사용
(2) 카멜 표기법 또는 스네이크 표기법 사용
(3) 예약어 사용 금지
    : print, True, False, None ... 등등
(4) 특수문자 사용 금지, 단 언더바(_)는 사용 가능
'''

#변수 : 데이터를 저장하는 공간
#변수를 사용하는 이유: 데이터 재사용 및 프로그램을 효율적으로 관리하기 위함
intro = "Hello World"
print(intro)
print(intro)
print(intro)
print(intro)
print(intro)

num1 = 10
num2 = 20

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

number = 20

name = "hong gil dong"
age = 21
address = 'korea, Seoul'

print(name)
print(age)
print(number)

print(name)
print(age)
print(number)

#다음의 문구를 재출력한다고 했을 때, 변수를 사용해보자

name = '홍길동'


print(name, '고객님께')
print(name, '고객님 안녕하세요')
print('고객님께서 접수하신 A/S건에 대해서 연락을 드렸으나 연락이 어려워 메일 드립니다.')
print('A/S 접수 내용')
print('-----------------------------------------')
print('성함 : ',name)
print('내용 : 에어컨 고장')
print('-----------------------------------------')
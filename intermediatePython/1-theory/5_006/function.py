# 전역변수
# 함수 밖에서 선언된 변수로 어디에서나 사용은 가능하지만, 함수 안에서 수정할 수는 없다.
print('*'*30)
print('전역변수 예제')
print('*'*30)
num_out = 10
def outNumbers():
    num_out = 30
    print(f'함수 내부 num_out : {num_out}')

outNumbers()
print(f'전역 변수 num_out : {num_out}')

print()
# 지역변수
# 함수 안에 선언된 변수로 함수 안에서만 사용 가능하다.
print('*'*30)
print('지역변수 예제')
print('*'*30)
def inNumbers():
    num_in = 20
    print(f'함수 내부 num_in : {num_in}')

inNumbers()
# print(f'지역 변수 num_in : {num_in}) >> name 'num_in' is not defined
print()

# global
# 함수 안에서도 전역변수의 값을 수정할 수 있다.
print('*'*30)
print('global 예제')
print('*'*30)
num_global = 10
def globalNumbers():
    global num_global
    num_global = 14235
    print(f'함수 내부 num_global : {num_global}')

globalNumbers()
print(f'global 변수 : {num_global}')
print()

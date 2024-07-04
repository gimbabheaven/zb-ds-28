# 중첩 함수
# 내부 함수를 함수 밖에서 호출할 수 없다.
# 함수 안에 또 다른 함수가 있는 형태

def out_function():
    print('out_function called')

    def in_function():
        print('in_function called')
    
    in_function()

out_function()
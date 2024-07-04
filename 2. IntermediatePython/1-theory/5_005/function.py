# 함수 실행 결과 반환
# return 키워드를 이용하면 함수 실행 결과를 호출부로 반환할 수 있다.

def calculator(n1, n2):
    result = n1 + n2
    return result

print(calculator(10, 20))

returnValue = calculator(10, 20)
print(returnValue)


# 함수가 return을 만나면 실행을 종료한다.

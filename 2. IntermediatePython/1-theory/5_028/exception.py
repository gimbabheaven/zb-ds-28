# 예외(exception) : 문법적인 문제는 없으나 실행 중 발생하는 예상하지 못하는 문제
# 예외 관련 클래스는 Exception을 상속받는다

def add(n1, n2):
    print(n1 + n2)

def div(n1, n2):
    print(n1 / n2)

fn = int(input('first : '))
fn = int(input('second : '))

add
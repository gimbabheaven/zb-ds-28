# 함수 내에서 또다른 함수 호출
def fun1():
    print('1: fun1 호출')
    fun2()
    print('4: fun2 호출 후 실행됨')

def fun2():
    print('2: fun2 호출')
    fun3()

def fun3():
    print('3: fun3 호출')

fun1()


# pass를 이용해서 실행문을 생략할 수 있다.

def printTodayWeather():
    print('오늘 날씨는 매우 좋아요.')
    tomorrowWeather()

def tomorrowWeather():
    pass

printTodayWeather()
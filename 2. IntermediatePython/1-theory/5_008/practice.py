# 삼각형, 사각형, 원의 넓이를 반환하는 lambda 함수

triangle = lambda n1, n2 : (n1 * n2) / 2
square = lambda n1, n2 : n1 * n2
circle = lambda n3 : n3 * n3 * 3.14

n1 = 20
n2 = 30
n3 = 6
triangleArea = triangle(n1, n2)
squareArea = square(n1, n2)
circleArea = circle(n3)

print(
    '삼각형 : {}\n사각형 : {}\n원 : {}'.format(triangleArea, squareArea, circleArea)
)
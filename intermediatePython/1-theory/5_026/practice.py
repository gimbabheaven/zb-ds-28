'''
삼각형 넓이를 계산하는 클래스를 만들고, 이를 상속하는 클래스에서
getArea()를 오버리이딩해서 출력 결과가 다음과 같을 수 있도록 클래스를 만들어보자
'''

class Triangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def printTriangle(self):
        print(f'widfh : {self.width}')
        print(f'height : {self.height}')

    def getArea(self):
        area = self.width * self.height / 2
        return area
    
class TriangleArea(Triangle):
    def __init__(self, w, h):
        super().__init__(w, h)

    def getArea(self):
        pass


triangle = TriangleArea(10, 5)

print(triangle.printTriangle())
print(triangle.getArea())
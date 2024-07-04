# super() : 상위 클래스의 속성을 초기화하기 위해서 super()을 이용한다.

class P_Class:
    def __init__(self, pNum1, pNum2):
        print('[pClass] __init__()')
        self.pNum1 = pNum1
        self.pNum2 = pNum2

class C_Class(P_Class):

    def __init__(self, cNum1, cNum2):
        print('[cClass] __init__()')

        #P_Class.__init__(self, cNum1, cNum2) #부모 클래스 초기화
        super().__init__(cNum1, cNum2)
        
        self.cNum1 = cNum1
        self.cNum2 = cNum2

cls = C_Class(10, 20)

class Calculator:

    def __init__(self):
        self.number1 = 0
        self.number2 = 0
        self.result = 0

    def add(self):
        self.result = self.number1 + self.number2
        return self.result
    
    def sub(self):
        self.result = self.number1 - self.number2
        return self.result
    
    def mul(self):
        self.result = self.number1 * self.number2
        return self.result
    
    def div(self):
        self.result = self.number1 / self.number2
        return self.result
    
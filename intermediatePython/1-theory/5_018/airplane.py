class Airplane:
    def __init__(self, company, number):
        self.company = company
        self.number = number

    def printInfo(self):
        print(f'this airplane is : {self.company} {self.number}')

airplane1 = Airplane('Boeing', 747)
airplane2 = Airplane('Boeing', 777)
airplane3 = Airplane('Airbus', 300)
airplane4 = Airplane('Airbus', 350)

print('-'*30)
airplane1.printInfo()
print('-'*30)
airplane2.printInfo()
print('-'*30)
airplane3.printInfo()
print('-'*30)
airplane4.printInfo()
print('-'*30)
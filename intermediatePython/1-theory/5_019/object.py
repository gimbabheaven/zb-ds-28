# 객체 속성 변경
class NewGenerationPc:

    def __init__(self, name, cpu, memory, ssd):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.ssd = ssd
    
    def doExcel(self):
        print('RUN EXCEL!!')

    def doPhotoshop(self):
        print('RUN PHOTOSHOP!!')

    def printPcInfo(self):
        print('-'*30)
        print(f'name : {self.name}')
        print(f'cpu : {self.cpu}')
        print(f'memory : {self.memory}')
        print(f'ssd : {self.ssd}')
        print('-'*30)
    
myPC = NewGenerationPc('myPc', 'i5', '16GB', '256G')
myPC.printPcInfo()

friendPC = NewGenerationPc('myPC', 'i7', '32G', '512G')
myPC.printPcInfo()
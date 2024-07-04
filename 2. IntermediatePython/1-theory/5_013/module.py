import unitConversion as uc


inputNumber = int(input('길이(cm) 입력 : '))

returnValue = uc.cmToMm(inputNumber)
print(f'cm -> mm : {returnValue}mm')
returnValue = uc.cmToInch(inputNumber)
print(f'cm -> inch : {returnValue}inch')
returnValue = uc.cmToM(inputNumber)
print(f'cm -> m : {returnValue}m')
returnValue = uc.cmToFt(inputNumber)
print(f'cm -> ft : {returnValue}ft')
def cmToMm(n):
    return round(n * 10, 3)

def cmToInch(n):
    return round(n * 0.393, 3)

def cmToM(n):
    return round(n * 0.01, 3)

def cmToFt(n):
    return round(n * 0.032, 3)

if __name__ == '__main__':
    print(f'10cm : {cmToMm(22)}mm')
    print(f'10cm : {cmToInch(22)}inch')
    print(f'10cm : {cmToM(22)}m')
    print(f'10cm : {cmToFt(22)}ft')

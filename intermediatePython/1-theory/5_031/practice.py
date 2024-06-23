evenList = []
oddList = []
floatList = []
dataList = []

n = 1
while n < 6:
    try:
        data = input('input number :')
        floatNum = float(data)
    except:
        print('예외 발생')
        continue
    else:
        if floatNum - int(floatNum) != 0:
            print('float number!')
            floatList.append(floatNum)
        else:
            if(floatNum) % 2 == 0:
                print('even number!')
                evenList.append(floatNum)
            else:
                print('odd number!')
                oddList.append(floatNum)
        n += 1

    finally:
        dataList.append(data) # 무조건 실행
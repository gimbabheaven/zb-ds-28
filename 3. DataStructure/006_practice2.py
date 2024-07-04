classCnts = [[1, 18]
            , [2, 19]
            , [3, 23]
            , [4, 21]
            , [5, 20]
            , [6, 22]
            , [7, 17]]

minCnts = 0
minCls = 0
maxCnts = 0
maxCls = 0

for clas, cnts in classCnts:
    if clas == 1:
        minCnts = cnts
        maxCnts = cnts
    if cnts <= minCnts:
        minCnts = cnts
        minCls = clas
    if cnts >= maxCnts:
        maxCnts = cnts
        maxCls = clas

print('max : {} 반 // {} 명'.format(maxCls, maxCnts))
print('min : {} 반 // {} 명'.format(minCls, minCnts))
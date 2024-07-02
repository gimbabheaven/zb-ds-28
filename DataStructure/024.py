tup1 = ('홍길동', '박찬호', '이용규')
tup2 = ('박승철', '김지은', '강호동')
print(tup1)
print(tup2)
print()
result = tup1 + tup2
print(result)

print()
print()
print()

myNumbers = (1, 3, 5, 6, 7)
friendNumbers = (2, 3, 5, 8, 10)

for number in friendNumbers:
    if number not in myNumbers: #친구의 번호가 나에게 없다면,
        myNumbers = myNumbers + (number, ) #number를 튜플로 변환
    
print(myNumbers)

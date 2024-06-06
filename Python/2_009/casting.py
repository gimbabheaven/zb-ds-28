#빈 문자 VS 공백 문자
'''
'' : 데이터 없음
' ' : 공백 데이터 있음
'''

var = ''
print(var)
print(type(var))

var = bool(var)
print(var)
print(type(var))

varb = ' '
print(varb)
print(type(varb))

var1 = bool(varb)
print(varb)
print(type(varb))

print()
print()

#문자 > 논리형 > 산술연산
var1 = 'True'
var2 = 'False'

print(var1)
print(var2)
print(type(var1), type(var2))

var1 = bool(var1)
var2 = bool(var2)
print(var1, var2) #데이터가 존재하면 True
print(type(var1), type(var2))

print(var1 + var2) # True = 1이므로 1+1 = 2

print()
print()

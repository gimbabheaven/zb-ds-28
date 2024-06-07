'''
실내 온도를 입력하고 온도가 28'C 이상이면 '냉방 작동!'이 출력되고,
20'C이하면 '난방 작동!'이 출력되는 코드
'''
import operator

tmp = int(input('실내 온도 입력 : '))

ice = 28
hot = 20

if operator.ge(tmp, ice):
    print('냉방 작동!')
elif operator.le(tmp, hot):
    print('난방 작동!')
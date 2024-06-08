'''
적설량을 입력하고 적설량이 30mm이상이면 대설 경보를 발령하고,
그렇지 않으면 대설 경보를 해제하는 코드
'''
import operator

snowAmount = int(input('적설량을 입력하세요 : '))
alert = 30

print('!!** 대설 경보 **!!') if operator.ge(snowAmount, alert) else print('** 경보 해제 **')
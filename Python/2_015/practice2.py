'''
123개의 사과를 4개씩 직원들에게 나누어 주려고 한다.
최대 나누어 줄 수 있는 직원 수와 남는 사과 갯수를 출력해 보자
'''

emp = 123
part = 4

result = divmod(emp, part)
print('직원 수 : {}\n남는 사과 : {}'.format(result[0], result[1]))
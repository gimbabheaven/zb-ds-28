# extend

group1 = ['A', 'B', 'C']
group2 = ['D', 'E', 'F']
print(f'group1 : {group1}')
print(f'group2 : {group2}')

group1.extend(group2)
print(f'group1 : {group1}')
print(f'group2 : {group2}')

result = group1 + group2
print(f'rseult : {result}')

group3 = [1, 2, 3]
group4 = [4, 5, 6]
print(f'group3 : {group3}')
print(f'group4 : {group4}')
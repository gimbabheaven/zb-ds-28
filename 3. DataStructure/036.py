scores = {'kor':88,
          'eng':55,
          'mat':85,
          'sci':57,
          'his':82}

print('all : ', scores)

ks = scores.keys()
vs = scores.values()
its = scores.items()

print()
print(f'{type(ks)} : {ks}')
print(f'{type(vs)} : {vs}')
print(f'{type(its)} : {its}')
print()
print(f'{type(list(ks))} : {list(ks)}')
print()

for key in ks:
    print(key)
print()
for value in vs:
    print(value)
print()
for item in its:
    print(item)
print()
for key in scores.keys():
    print(scores[key])
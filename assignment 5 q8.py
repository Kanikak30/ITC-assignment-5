enter = list(map(int, input('Enter 10 numbers : ').split()))

P = []
N = []
O = []
E = []

for i in enter:
    if i > 0: P.append(i)
    if i<0: N.append(i)
    if i%2 == 0: E.append(i)
    else: O.append(i)
#a)
print('Positive: ', P)
#b)
print('Negative: ', N)
#c)
print('Odd: ', O)
#d)
print('Even: ', E)
for i in set(enter):
    print(i, 'Occurs :', enter.count(i), 'Times')

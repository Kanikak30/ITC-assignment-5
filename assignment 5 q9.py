strg = ' '.join(input("Enter some words: ").split())
line = strg.split()
for i in set(line):
    print(i, 'Occurs:',line.count(i), 'Times')

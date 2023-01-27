line1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
line2 = list(map(str,line1))
#print(line2)

rangee = int(input("Enter rows:"))
p = 0
q = 1
letters = ((rangee)*(rangee + 1))//2
if letters > 26:
    line1 *= (letters//26) + 1
    line2 = list(map(str,line1))
for i in range(rangee):
    q = p + i+ 1
    print(line1[p:q])
    p += i + 1

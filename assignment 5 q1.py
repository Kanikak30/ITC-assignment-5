inp = input("Enter string: ")
line1 = []
for i in range(len(inp)):line1.append(inp[-(i+1)])
print(''.join(line1))

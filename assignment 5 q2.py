one = input('Enter range in format(x y) : ').split()  
two = list(map(int,one))
thr = int(input('Enter number : '))
for i in range(two[0], two[1] + 1): 
    if(i%thr == 0):print(i, end=' ')

alpha = input('Enter range in format(x y) : ').split()  
beta = list(map(int,alpha))


for numb in range(beta[0], beta[1] + 1): 
    prime = True
    if numb == 1:
        prime = False
    elif numb > 1:
    # check for factors
        for i in range(2, numb):
            if (numb % i) == 0:
                prime = False
                break
    if(prime):print(numb)

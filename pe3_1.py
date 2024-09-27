
factors= []
x= 600851475143
i=1

while (x>1):
    i+=1
    if (x%i == 0):
        if i not in factors:
            factors.append(i)
        x = x/i 
        i = 1
        
    

print(factors)

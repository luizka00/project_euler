def test_func(func):
    x= (func(10) == 23)

    if x == True:
        print("Test passed")

    else:
        print("Test NOT passed")

        #function to test if our function is correct


def sum_of_multiples(x):
    sum=0
    i=1
    while(i<x):
        if (i%3==0) or (i%5 == 0):
            sum +=i
        i+=1  

    return(sum)


print(sum_of_multiples(1000))
test_func(sum_of_multiples)

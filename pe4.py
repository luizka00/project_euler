"""A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is 9009 = 91 times 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def find_largest():

    largest= []
    """for each pallindrome check if it's a product of 3 digit numbers"""
    candidate= list(str(998001))
    while ( 100000 <= candidate <= 998001):
        if (candidate[0] == candidate[5] and candidate[1] == candidate[4] and candidate[2] == candidate[3]):
            check_if_product(candidate)
        
        


    
def check_if_product():
    pass



largest_number= 998001

print(list(str(largest_number)))
candidate= list(str(998001))
print(type(int(candidate[0])))
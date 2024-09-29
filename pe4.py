"""A palindromic number reads the same both ways. The largest palindrome made from the product of two $2$-digit numbers is 9009 = 91 times 99
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(n):
    # Check if n is a palindrome by comparing it to its reverse
    return str(n) == str(n)[::-1]

def largest_palindrome_product():
    max_palindrome = 0
    
    # Iterate through all 3-digit numbers
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):  # Start j from i to avoid repeating pairs
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
                
    return max_palindrome

# Find the largest palindrome made from the product of two 3-digit numbers
result = largest_palindrome_product()
print(result)
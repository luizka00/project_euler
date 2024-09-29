"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def find_prime(x):
    """Iterates numbers between 2 and x, checks each if it's prime, if it is, increments the number of primes found"""
    i=2
    primes_found=0
    while (primes_found < x):
        if is_prime(i) == True:
            primes_found +=1
        i+=1 
    return i-1




def is_prime(n): 
    """Checks if the given numebr is  a prime number"""
    # Check if number is less than 2
    if n <= 1:
        return False
    # Check for divisors from 2 to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(find_prime(10001))
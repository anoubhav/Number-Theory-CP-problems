# Time complexity: O(Nlog(log N)); Space complexity: O(N).
# application: If you have q queries, q<=10**6. For each query determine if n is prime, where n<=10**7.
# Then using basic primality test each time will yield a complexity of O(q*sqrt(n)). This will give TLE. 
# So instead we can precompute using sieve for all N numbers.


# The idea behind is this: A number is prime, if none of the smaller prime numbers divides it. Since we iterate over the prime numbers in order, we already marked all numbers, who are divisible by at least one of the prime numbers, as divisible. Hence if we reach a cell and it is not marked, then it isn't divisible by any smaller prime number and therefore has to be prime.


# If the current number i is a prime number, it marks all numbers that are multiples of i as composite numbers, starting from i^2. This is already an optimization over naive way of implementing it, and is allowed as all smaller numbers that are multiples of i necessary also have a prime factor which is less than i, so all of them were already sifted earlier.

# Uses only odd numbers and a concept called bytearray
def sieve_fastest(lim):
    from itertools import compress
    # Find all primes upto n  (including n). NOTE: it does not include 2; To get list, convert the return value to list.
    BA = bytearray
    n = (lim-1)//2
    prime = BA([1])*(n+1)
    prime[0] = 0 # 2*0+1 = 1 n'est pas premier

    for i in range((int(lim**0.5)+1)//2):
        if prime[i]:
            p = 2*i+1 # p is prime
            i2 = i*(i+1)<<1
            prime[i2::p]=BA(1+ (n-i2)//p )
    return compress(range(1,lim+1,2),prime)

# Src: https://projecteuler.net/overview=010
# An easy optimisation of the sieve is suggested by the discrimination of odd and even numbers. Apart from 2, all that the even numbers do is being crossed out once and occupying space.  If we get rid of the even numbers, we save (limit − 2)/2 crossings out and, more importantly, we use only half the memory. 
def sieve_optimized(n):
    # Find all primes upto n  (including n)
    sievebound = (n-1)//2
    sieve = [False]*(sievebound + 1)
    sieve[0] = True
    crosslimit = (int(sievebound**0.5) - 1)
    for i in range(1, crosslimit + 1):
        if not sieve[i]:
            for j in range(2*i*(i+1), sievebound + 1, 2*i+1):
                sieve[j] = True
    
    return [2] + [2*i+1 for i in range(1, sievebound+1) if not sieve[i]]

def sieve(n):
    is_prime = [1]*(n + 1)
    is_prime[0], is_prime[1] = 0, 0

    for num in range(2, n+1):
        if num*num>n:
            break

        if is_prime[num]:
            for mult in range(num*num, n+1, num):
                is_prime[mult] = 0

    primes = [i for i in range(n+1) if is_prime[i]]
    return primes

from time import time
n = 10000000

# 200ms for 10^7
t = time()
print(len(list(sieve_fastest(n))) + 1) # it does not include 2.
print(time() - t)

# 920ms
t = time()
print(len(sieve_optimized(n)))
print(time() - t)

#1830ms
t = time()
print(len(sieve(n)))
print(time() - t)



# Code from https://projecteuler.net/overview=010
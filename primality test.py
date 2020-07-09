# Check if the number is prime
from sys import stdin

def naive(n):
    # O(n) time complexity; O(1) space
    if n==1: return False

    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def good(n):
    # O(sqrt n) time complexity; O(1) space
    if n ==1: return False
    i = 2
    # a number has at most 1 prime factor greater than sqrt n.
    while i*i<=n:
        if n%i == 0: return False
        i+=1

    return True

def better(n):
    if n ==1: return False
    if n == 2: return True
    # only 2 is even prime factor
    i = 3
    while i*i<=n:
        if n%i == 0: return False
        i+=2
    return True

def best(num):
    if num == 1: return False
    elif num < 4: return True
    elif num%2 == 0 or num%3 == 0: return False
    else:
        for i in range(5, int(num**0.5) + 1, 6):
            if num%i==0:return False
            if num%(i+2)==0:return False
        return True

# n = 305175781
n = 1000000000100011
# True 5.341723203659058
# True 2.703773260116577
# True 1.1240077018737793

from time import time
# t = time()
# print(naive(n), time() - t) # 20 s for 305175781
t = time()
print(good(n), time() - t)  # 0.002 s
t = time()
print(better(n), time() - t) # 0. 00099
t = time()
print(best(n), time() - t) # 0. 00099


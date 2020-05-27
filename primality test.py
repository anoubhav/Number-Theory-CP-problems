# Check if the number is prime
from sys import stdin

# n = int(stdin.readline())
# n = 12207031
n = 305175781

def naive(n):
    # O(n) time complexity; O(1) space
    if n==1: return False

    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def better(n):
    # O(sqrt n) time complexity; O(1) space
    if n ==1: return False
    i = 2
    while i*i<=n:
        if n%i == 0: return False
        i+=1

    return True

from time import time
t = time()
print(naive(n), time() - t) # 20 s
t = time()
print(better(n), time() - t) # 0.04 s


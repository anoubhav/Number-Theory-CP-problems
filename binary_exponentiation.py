# could not solve. Very interesting math question.
from time import time
def power(a, b):
    if b == 0:
        return 1
    if b%2==0:
        return (power(a, b//2))**2
    else:
        return a*(power(a, b//2))**2


def naive(a, b):
    ans = 1
    for _ in range(b):
        ans*=a
    return ans

# 8 100000
a, b = map(int, input().split())
t1 = time()
r1= power(a, b)
t2 = time()
r2= naive(a, b)
t3 = time()
r3 = pow(a, b)

print('Binary exponentiation:', t2-t1)
print('Naive:', t3- t2)
print('Inbuilt:', time()-t3)
assert r1 == r2 == r3
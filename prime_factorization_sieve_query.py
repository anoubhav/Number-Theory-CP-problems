from random import randint
def sieve_optimized(limit):
    # Preprocessing step takes O(N log log N) time complexity.
    n = limit
    # Filimitd all primes upto n  (including n)
    sievebound = (n-1)//2
    sieve = [-1]*(sievebound + 1)
    # sieve[0] = True
    crosslimit = (int(sievebound**0.5) - 1)
    for i in range(1, crosslimit + 1):
        if sieve[i] == -1:
            for j in range(2*i*(i+1), sievebound + 1, 2*i+1):
                sieve[j] = 2*i + 1
    return sieve

def factorization(n, sieve):
    # Factorisaton query takes O(log N) time after preprocessing.
    divs = [1]
    while n!=1:
        if n&1:
            div = sieve[(n-1)//2]
            if div == -1:
                divs.append(n)
                break
            else:
                n //= div
                divs.append(div)
        else:
            n >>= 1
            divs.append(2)

    return divs

queries = 10**2
maxnum = 10**8

# Precompute using sieve upto maxnum in O(N log log N) time. The factorisation of each number upto maxnum can be obtained in O(log N) time instead of O(sqrt(N))
sieve = sieve_optimized(maxnum)
print('Pre-computation over')

while queries:
    n = randint(1, maxnum)
    print(f'number {n}: {factorization(n, sieve)}')
    queries -= 1





# Time complexity: O(Nlog(log N)); Space complexity: O(N).
# application: If you have q queries, q<=10**6. For each query determine if n is prime, where n<=10**7.
# Then using basic primality test each time will yield a complexity of O(q*sqrt(n)). This will give TLE. 
# So instead we can precompute using sieve for all N numbers.

n = 10**4

is_prime = [1]*(n + 1)
is_prime[0], is_prime[1] = 0, 0

for num in range(2, n+1):
    if num*num>n:
        break

    if is_prime[num] == 0:
        continue

    for mult in range(2*num, n+1, num):
        is_prime[mult] = 0

primes = [i for i in range(n+1) if is_prime[i]]
print(*primes)
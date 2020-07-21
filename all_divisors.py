from math import sqrt, floor
def all_divisors(n):
    divs = [1]
    if n&1: start, step = 3, 2
    else: start, step = 2, 1

    for i in range(start, floor(sqrt(n)) + 1, step):
        if n%i == 0:
            if n//i!=i:
                divs += [i, n//i]
            else:
                divs += [i]
    divs.append(n)
    return divs

def sum_of_divisors(n):
    # Calculate the sum of divisors (all EXCLUDING the number itself, INCLUDING 1) upto n using sieve
    s = [1]*(n+1)
    s[0], s[1] = 0, 0

    for i in range(2, int(n**0.5)+1):
        s[i*i] += i
        for j in range(i*i+i, n+1, i):
            s[j] += i + j//i
    return s

print(sum_of_divisors(20))
print(*all_divisors(26))
print(*all_divisors(105))

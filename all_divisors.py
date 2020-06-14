from math import sqrt, floor
def divisors(n):
    divs = []
    for i in range(2, floor(sqrt(n)) + 1):
        if n%i == 0:
            if n//i!=i:
                divs += [i, n//i]
            else:
                divs += [i]
    return divs

print(*divisors(6))
def fibo_iter(n):
    if n<=2: return 1
    a, b = 1, 1
    index = 2
    while index<n:
        a, b = b, a + b
        index += 1
    return b

def fibo_Binet(n):
    from decimal import Decimal, getcontext
    # set the precision of division

    getcontext().prec = n

    sqrt5 = Decimal(5).sqrt()
    phi = (1 + sqrt5)/Decimal(2.0)

    return round(((phi**n) - (1-phi)**n)/ sqrt5)

n = 100
print(fibo_iter(n))
print(fibo_Binet(n))
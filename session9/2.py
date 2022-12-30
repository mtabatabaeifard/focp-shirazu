def fact(n):#non-recursive
    f = 1
    if n == 0:
       print('1')
    else:
        for i in range(1,n+1):
            f *= i
        print(f)

print(fact(3))


def fact_rec(n):#recursive
    if n == 1:
        return 1
    else:
        return n * fact_rec(n-1)

print(fact_rec(3))
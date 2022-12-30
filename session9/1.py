def fibo(n): #non-recursive
    r = []
    a = 0
    b = 1
    while a < n:
        r.append(a)
        a,b = b,a+b
    return r

print(fibo(10))

def fibo_rec(n):#recursive
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibo_rec(n-1)+fibo_rec(n-2))

print(fibo_rec(4))
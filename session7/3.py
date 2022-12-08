def prod(lst):
    prod=1
    for i in range(len(lst)):
        prod *= lst[i]
    return prod

print(prod([4,5,3]))
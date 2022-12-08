def max(lst):
    max = lst[0]
    for i in lst:
        if i >= max :
            max = i
    return max

print(max([10,500,1500,1401,2,0]))
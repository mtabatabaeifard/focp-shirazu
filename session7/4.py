def min(lst):
    min = lst[0]
    for i in lst:
        if i <=min:
            min = i
    return min

print(min([10,1564564,1456458,12,5,2]))
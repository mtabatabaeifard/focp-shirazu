def mean(lst):
    sum_of_lst = sum(lst)
    mean = sum_of_lst/len(lst)
    return mean

print(mean([10,6,14,23,150000]))
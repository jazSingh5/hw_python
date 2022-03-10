

def sort_list(lst):

    n = len(lst)
    i = 1

    while (i < n):
        d = 0
        while (d <= n-i-1):
            if (lst[d+1] > lst[d]):
                lst[d+1], lst[d] = lst[d+1], lst[d]
            d += 1
        i += 1
    return lst




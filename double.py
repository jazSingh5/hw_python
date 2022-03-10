def sort_list(lst):

    n = len(lst)
    i = 1

    while (i < n):
        d = 0
        while (d <= n-1):
            if (lst[i] > lst[d]):
                lst[i], lst[d] = lst[d], lst[i]
            d += 1
        i += 1
    return lst

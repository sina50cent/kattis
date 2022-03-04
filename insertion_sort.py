def insertion_sort(lst):
    for k in range(1,len(lst)):
        cur = lst[k]
        j = k
        while j > 0 and lst[j - 1] > cur:
            lst[j] = lst[j-1]
            j-=1
        lst[j] = cur
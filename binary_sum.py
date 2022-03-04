def binary_sum(s,start,stop):
    if start >= stop:
        return 0
    elif start == stop - 1:
        return s[start]
    mid = (start+stop)//2
    return binary_sum(s,start,mid) + binary_sum(s,mid,stop)


print(binary_sum([1,2,3,4,5],0,len([1,2,3,4,5])))
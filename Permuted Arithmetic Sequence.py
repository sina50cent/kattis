res = []
def check_artmetic(lst):
    deff = lst[1] - lst[0]
    for i in range(len(lst)):
        if i+1<= len(lst) -1 and lst[i + 1] - lst[i] != deff:
            return None
    return 1

for i in range(int(input())):
    temp = list(map(int, input().split()))[1:]
    # temp1 = sorted(temp)
    if check_artmetic(temp):
        res.append('arithmetic')
    elif check_artmetic(sorted(temp)):
        res.append('permuted arithmetic')
    else:
        res.append('non-arithmetic')
print(*res, sep='\n')
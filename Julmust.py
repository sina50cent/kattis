def binary_search(lst, key, b, e):
    if b > e:
        return False
    m = (e - b) // 2 + b
    if key == lst[m]:
        print(lst[m])
        print('exact',flush=True)
        return
    elif key < lst[m]:
        print(lst[m])
        print('less',flush=True)
        binary_search(lst, key, b, m - 1)
    else:
        print(lst[m])
        print('more',flush=True)
        binary_search(lst, key, m + 1, e)



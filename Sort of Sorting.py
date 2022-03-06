while True:
    n = int(input())
    lst = []
    if n == 0:
        break
    for i in range(n):
        lst.append(input())
    lst.sort(key=lambda x:x[0:2])
    for i in lst:
        print(i)
    print()

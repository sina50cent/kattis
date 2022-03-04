while True:
    try:
        lst = list(map(int,input().split()))
    except EOFError:
        break

    print(abs(lst[0] - lst[1]))
    
n = int(input())
lst = list(map(int,input().split()))
lst.sort()
lst_asd = []


def print_format(lst):
    for i in range(len(lst) - 1):
        if lst[i] == '-':
            print('', end='')
        elif lst[i] != '-' and lst[i + 1] == '-' and i != len(lst) - 1:
            print(lst[i], end='-')
        else:
            print(lst[i], end=' ')
    print(lst[len(lst) - 1])


for i in range(len(lst)):
    if i == 0:
        lst_asd.append(lst[0])
    elif lst[i] - lst[i - 1] == 1 and lst[i + 1] - lst[i] == 1:
        lst_asd.append('-')
    else:
        lst_asd.append(lst[i])


print_format(lst_asd)


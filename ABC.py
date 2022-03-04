lst = list(map(int,input().split()))
order = input()
a = min(lst)
lst.remove(a)
c = max(lst)
lst.remove(c)
b = lst[0]
lst_a = []
for i in order:
    if i == 'A':
        lst_a.append(str(a))
    elif i == 'B':
        lst_a.append(str(b))
    else:
        lst_a.append(str(c))

print(' '.join(lst_a))
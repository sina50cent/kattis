lst_asw = []
for i in range(5):
    lst = list(map(int,input().split()))
    lst_asw.append(sum(lst))
max = lst_asw[0]
n = 0
for i in range(len(lst_asw)):
    if max < lst_asw[i]:
        max = lst_asw[i]
        n = i

print(n + 1 , max)
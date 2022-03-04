
lst = []

for _ in range(int(input())):
    lst.append(int(input()))


lst.sort()
lst.reverse()

cost = 0
for i in range(len(lst)):
    if i % 3 != 2:
        cost += lst[i]
print(cost)
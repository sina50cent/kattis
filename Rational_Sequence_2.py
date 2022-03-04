def rational(p,q):
    if p == 1 and q == 1:
        return 1
    if p > q:
        return 2*(rational(p-q,q)) + 1
    else:
        return 2*(rational(p, q-p))


x = int(input())
lst = []
for i in range(x):
    row , y = input().split()
    lst.append(y)

answer_lst = []

for i in lst:
    p ,q = i.split("/")
    answer_lst.append(rational(int(p),int(q)))

for i in range(len(answer_lst)):
    print(i+1,answer_lst[i])
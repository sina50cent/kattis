def rational(p,q,n):

    if n == 1:
        p, q = 1, 1
        return p,q
    elif n % 2 == 0 :
        p , q = rational(p , q ,n / 2)
        return  p,p + q
    else:
        p , q = rational(p , q ,n // 2)
        return p + q,q

lst = []
x = int(input())
for i in range(x):
    row , y = map(int,input().split())
    lst.append(y)

answer_lst = []
# p, q = rational(0, 0, 1431655765)
for i in lst:
    p, q = rational(0, 0, i)
    answer_lst.append(f"{p}/{q}")

for j in range(len(answer_lst)):
    print(j+1,answer_lst[j])
# print(f"{p}/{q}")
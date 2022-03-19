lst = []
for i in range(int(input())):
    n = int(input())
    lst.append(f"{n} is even" if n % 2 == 0 else f"{n} is odd")

print(*lst,sep="\n")
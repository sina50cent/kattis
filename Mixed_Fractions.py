def mix_fractions(x,y):
    return f"{x // y} {x % y} / {y}"


lst = []
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    lst.append(mix_fractions(x, y))

for i in lst:
    print(i)
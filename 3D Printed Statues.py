statues = int(input())
printer = 1
day = 0
while statues >= 1:
    if printer + 1 < statues and statues - printer > 2:
        printer += 1
        day += 1
        continue
    statues -= printer
    day += 1

print(day)
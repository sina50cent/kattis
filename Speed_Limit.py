n = int(input())

lst = []
while n != -1:
    total_distance = 0
    old_time = 0
    for i in range(n):
        speed , time = list(map(int,input().split()))
        total_distance += (speed * (time - old_time))
        old_time = time
    lst.append(f'{total_distance} miles')
    n = int(input())


print(*lst,sep='\n')
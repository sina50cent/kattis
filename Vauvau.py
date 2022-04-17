dog_time = list(map(int,input().split()))
pmg = list(map(int,input().split()))

pmg.sort()
dog_time.sort()
# print(max(pmg))
n = 1

status = 'both'
pmg_arrived = []


def find_index(lst,find):
    for i in range(len(lst)):
        if lst[i] == find:
            return i


def is_find(lst,find):
    for i in range(len(lst)):
        if lst[i] == find:
            return 1


while n <= max(pmg):
    if is_find(pmg,n):
        pmg_arrived.append(status)

    if find_index(dog_time,n) == 1:
        status = 'one'
    elif find_index(dog_time,n) == 3:
        status = 'none'


    n += 1

print(*pmg_arrived,sep='\n')
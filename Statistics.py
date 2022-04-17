dct = {}
n = 1
while True:
    try:
        lst = list(map(int, input().split()))
        dct[f'Case {n}'] = [min(lst[1:]), max(lst[1:]), max(lst[1:]) - min(lst[1:])]
        n += 1
    except EOFError:
        break



# while n <= 4:
#     lst = list(map(int,input().split()))
#     dct[f'Case {n}'] = [min(lst[1:]), max(lst[1:]), max(lst[1:]) - min(lst[1:])]
#     n += 1

for key,value in dct.items():
    print(f'{key}:',*value)
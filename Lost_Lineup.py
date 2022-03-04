from itertools import permutations

key = input()
lst = [x for x in key]
big = []
for item in permutations(lst):
    if int(''.join(lst)) < int(''.join(item)):
        big.append(int(''.join(item)))

if len(big) > 0 :
    print(min(big))
else :
    print(0)
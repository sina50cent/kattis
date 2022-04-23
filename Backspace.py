entry = input()
lst = []
n = 0
while n < len(entry):
    if entry[n] == '<':
        lst.pop()
        n += 1
        continue
    lst.append(entry[n])

    n += 1
print(''.join(lst))

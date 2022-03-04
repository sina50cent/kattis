
lst=[]
for i in range(4):
    lst.append(list(map(int,input().split())))

n = int(input())
if n == 0:
    for i in range(len(lst)):
        for j in range(-1,-len(lst),-1):
            if j >= -len(lst[i]) + 1 and (lst[i][j - 1] == 0 or lst[i][j] == lst[i][j - 1]):
                lst[i][j - 1] += lst[i][j]
                lst[i][j] = 0

            if j == -1 and (lst[i][-4] == 0 or lst[i][-3] == lst[i][-4]):
                lst[i][-4] += lst[i][-3]
                lst[i][-3] = 0

            if j == -4 and lst[i][-2] == 0:
                lst[i][-2] += lst[i][-1]
                lst[i][-1]
elif n == 1:
    for i in range(4):
        for j in range(-1, -len(lst) - 1, -1):
            if j >= -len(lst[i]) + 2 and (lst[j - 1][i] == 0 or lst[j][i] == lst[j-1][i]):
                lst[j - 1][i] += lst[j][i]
                lst[j][i] = 0

            if j == -1 and (lst[0][i] == 0 or lst[0][i] == lst[1][i]):
                lst[0][i] += lst[1][i]
                lst[1][i] = 0

            if j == -4 and lst[-2][i] == 0:
                lst[-2][i] += lst[-1][i]
                lst[-1][i] = 0


    ...
elif n == 2:
    for i in range(len(lst)):
        for j in range(4):
            if j <= len(lst[i]) - 2 and (lst[i][j + 1] == 0 or lst[i][j] == lst[i][j + 1]):
                lst[i][j + 1] += lst[i][j]
                lst[i][j] = 0

            if j == 0 and (lst[i][3] == 0 or lst[i][3] == lst[i][2]):
                lst[i][3] += lst[i][2]
                lst[i][2] = 0

            if j == 3 and lst[i][1] == 0:
                lst[i][1] += lst[i][0]
                lst[i][0] = 0


else:
    for i in range(4):
        for j in range(4):
            if j <= len(lst[i]) - 2 and \
                    (lst[j + 1][i] == 0 or lst[j][i] == lst[j + 1][i]):
                lst[j + 1][i] += lst[j][i]
                lst[j][i] = 0

            if j == 0 and (lst[3][i] == 0 or lst[2][i] == lst[3][i]):
                lst[3][i] += lst[2][i]
                lst[2][i] = 0

            if j == 3 and lst[1][i] == 0:
                lst[1][i] += lst[0][i]
                lst[0][i]= 0
        if lst[2][i] == lst[3][i] or lst[3][i] == 0:
            lst[3][i] += lst[2][i]
            lst[2][i] = lst[1][i]
            lst[1][i] = lst[0][i]
            lst[0][i] = 0

        if lst[1][i] == lst[2][i] or lst[2][i] == 0:
            lst[2][i] += lst[1][i]
            lst[1][i] = lst[0][i]
            lst[0][i] = 0

        if lst[0][i] == lst[1][i] or lst[1][i] == 0:
            lst[1][i] += lst[0][i]
            lst[0][i] = 0


print(lst)

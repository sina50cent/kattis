jour = list(map(int,input().split()))
lst = []
while sum(jour) != 0:
    if sum(jour) == 13:
        lst.append('Never speak again.')
    elif jour[0] < jour[1]:
        lst.append('Left beehind.')
    elif jour[0] > jour[1]:
        lst.append('To the convention.')
    elif jour[0] == jour[1]:
        lst.append('Undecided.')
    jour = list(map(int,input().split()))
print(*lst,sep='\n')

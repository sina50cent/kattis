from math import pi

r, c = map(int,input().split())

ciclre_total = pi * (r ** 2)
crust = pi * ((r-c)**2)

print((crust / ciclre_total) * 100)


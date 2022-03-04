# def power_al(x,n):
#     if n == 1:
#         return x
#     return power_al(x,n-1) * x
#
#
# print(power_al(3,2))


# def power_al(x,n):
#     if n==0:
#         return 1
#     elif n % 2 ==0:
#         return power_al(x,n//2) ** 2
#     return x * (power_al(x,n//2) ** 2)
#
# print(power_al(2,3))


def power_(x,n): #book
    if n == 0:
        return 1
    else:
        partial = power_(x,n//2)
        result = partial * partial
        if n % 2 == 1:
            result *= x
        return result

print(power_(2,3))
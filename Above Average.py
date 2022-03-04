c = int(input())

lst_avg = []
lst_aws = []
for i in range(c):
    lst = list(map(int,input().split()))
    avg=sum(lst[1:]) / lst[0]
    lst_avg = [lst[i] for i in range(1,len(lst)) if lst[i] > avg]
    lst_aws.append('{a:.3f}%'.format(a=round((len(lst_avg) / lst[0]) * 100,3)))
for i in lst_aws:
    print(i)

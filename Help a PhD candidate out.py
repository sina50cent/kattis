lst_asw = []

for i in range(int(input())):
    num_test = input()
    if num_test[0].isnumeric():
        lst_asw.append(eval(num_test))
    else:
        lst_asw.append('skipped')

print(*lst_asw,sep='\n')
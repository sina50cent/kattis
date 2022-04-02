number_seedling = int(input())
seedling_day = list(map(int, input().split()))
seedling_day.sort(reverse=True)

min_day = 0
for i in range(number_seedling):
    if min_day < seedling_day[i] + i + 1:
        min_day = seedling_day[i] + i + 1

print(min_day + 1)
import sys

# input = sys.stdin.readline()

n = int(input())

arr = sorted(list(map(int, input().split())))

max_budget = int(input())

start = 0
end = max(arr)

budget = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2

    for x in arr:
        if x >= mid:
            total += mid
        else:
            total += x
    if total <= max_budget:
        budget = max(mid, budget)
    if total > max_budget:

        end = mid - 1
    else:
        start = mid + 1


print(budget)
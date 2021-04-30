import heapq

n = int(input())
# arr = deque()
arr = []
for i in range(n):
    arr.append(int(input()))

if n == 1:
    print(arr[0])
    exit()
res = 0
arr.sort()
heapq.heapify(arr)
while len(arr) != 1:
    a = heapq.heappop(arr)
    b = heapq.heappop(arr)
    heapq.heappush(arr,a+b)
    res += (a + b)

print(res)
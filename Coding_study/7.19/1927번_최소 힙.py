import heapq
import sys

input = sys.stdin.readline
n = int(input())
heap = []


for i in range(n):
    c = int(input())
    if c == 0:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)
    else:
        heapq.heappush(heap, c)
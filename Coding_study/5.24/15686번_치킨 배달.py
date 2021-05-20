from itertools import combinations

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


houses = []
chickens = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            houses.append([i,j])
        elif graph[i][j] == 2:
            chickens.append([i,j])

chicken_Case = combinations(chickens, m)
chicken_Case = list(chicken_Case)

min_chicken_dist = 999999
for chicken in chicken_Case:
    dist = 0

    for house in houses:
        dist_list = []
        for shop in chicken:
            dist_list.append(abs(house[0]-shop[0]) + abs(house[1] - shop[1]))
        dist += min(dist_list)

    if dist < min_chicken_dist:
        min_chicken_dist = dist

print(min_chicken_dist)
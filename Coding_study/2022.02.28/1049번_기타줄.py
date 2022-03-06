n, m = map(int, input().split())
pack = []
each = []

cost = 0

for i in range(m):
    a, b = map(int, input().split())
    pack.append(a)
    each.append(b)

c_pack = min(pack)
c_each = min(each)

if c_pack > c_each * 6:
    print(n * c_each)
    exit()

pack_first = n // 6
left = n % 6
cost += pack_first * c_pack

cost_plus_pack = cost + c_pack
cost += c_each * left

cost = min(cost, cost_plus_pack)
print(cost)
n = int(input())
s = int(input())


candidate = list(map(int, input().split()))

nominated = [ 0 for _ in range(n)]
photo = dict()


def get_key(a, val):
    for key, value in a.items():
         if val == value:
             return key

time = 0
for candy in candidate:
    time += 1
    if candy in photo:
        photo[candy] += 1
    else:
        if len(photo) >= n:
            del photo[get_key(photo, min(photo.values()))]
            photo[candy] = 1
        else:
            photo[candy] = 1
# list(photo)
# photo.sort()
name = []
for i in photo.keys():
    name.append(i)
name.sort()

print(*name)



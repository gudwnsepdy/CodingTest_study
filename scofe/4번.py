point = list(map(float, input().split()))
star =dict()
star['A'] = point[0]
star['B'] = point[1]
star['C'] = point[2]
star['D'] = point[3]
star['E'] = point[4]


n, m = map(int,input().split())

watched =[]
movie_type = []
for _ in range(n):
    watched.append(list(input().strip()))

for _ in range(n):
    movie_type.append(list(input().strip()))

rec = []

for i in range(n):
    for j in range(m):
        if watched[i][j] == 'Y':
            rec.append([movie_type[i][j], star[movie_type[i][j]],i,j,100])
        if watched[i][j] == 'O':
            rec.append([movie_type[i][j], star[movie_type[i][j]],i,j,200])

f = sorted(rec, key = lambda x : (x[4],-x[1], x[2], x[3]))
for case in f:
    print(case[0], case[1], case[2], case[3])

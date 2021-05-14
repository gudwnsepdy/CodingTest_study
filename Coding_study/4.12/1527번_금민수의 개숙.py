n, m = map(int, input().split())
cnt = 0
for i in range(n -1 , m):
    str_num = str(i)
    if '1' in str_num:
        continue
    elif '2' in str_num:
        continue
    elif '3' in str_num:
        continue
    elif '5' in str_num:
        continue
    elif '6' in str_num:
        continue
    elif '8' in str_num:
        continue
    elif '9' in str_num:
        continue
    elif '0' in str_num:
        continue
    cnt += 1
print(cnt)
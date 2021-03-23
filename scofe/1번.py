import sys
input = sys.stdin.readline

n = int(input())

time_table = []
for i in range(n):
    time = str(input())
    start, wave, end = map(str, time.split(" "))
    start_h, start_m = map(str, start.split(":"))
    if len(str(start_h)) < 2:
        start_h = "0" + str(start_h)
    if len(str(start_m)) < 2:
        start_m = "0" + str(start_m)
    end_h, end_m = map(str, end.split(":"))
    if len(str(end_h)) < 2:
        end_h = "0" + str(end_h)
    if len(str(start_m)) < 2:
        end_m = "0" + str(end_m)
    start_time = start_h + start_m
    end_time = end_h + end_m
    # time_table.append([start_h,start_m, end_h, end_m[:2]])
    time_table.append([str(start_time), str(end_time)])


star_time_r = max(time_table, key=lambda x: x[0])
end_time_r = min(time_table, key=lambda x: x[1])


if end_time_r[1] <= star_time_r[0]:
    print("-1")
else:
    # sh = int(star_time_r[0] /100 )
    sh = str(star_time_r[0])[:2]
    sm = str(star_time_r[0])[2:]
    eh = str(end_time_r[1])[:2]
    em = str(end_time_r[1])[2:]

    print(sh+":"+sm+" ~ "+eh+":"+em)
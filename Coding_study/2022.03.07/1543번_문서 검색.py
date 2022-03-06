long = str(input())
short = str(input())
prev_long = long

cnt = 0
while 1:
  long = long.replace(short, "*",1)

  if long == prev_long:
      break
  else:
      cnt += 1
  prev_long = long




print(cnt)
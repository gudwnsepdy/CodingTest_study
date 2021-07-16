import sys

input = sys.stdin.readline

a = list(input().strip())
b = list(input().strip())
# print(a,b)
stack = []
lb = len(b)
la = len(a)
for i in range(la):
    stack.append(a[i])
    # print(stack[-len(b):])
    if len(stack) >= lb and a[i] == b[-1]:
        if stack[-lb:] == b:
            # stack = stack[:-lb]
            del stack[-lb:]
            # print(stack,"dd")

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))

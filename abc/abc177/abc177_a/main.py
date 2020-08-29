d, t, s = map(int, input().split())

r = d//s
if d % s != 0:
    r += 1

if t >= r:
    print('Yes')
else:
    print('No')
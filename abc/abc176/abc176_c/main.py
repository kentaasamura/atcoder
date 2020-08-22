from sys import stdin
input = stdin.readline

n = input().rstrip()
a = list(map(int, input().split()))

ans = 0
for i in range(len(a)-1):
    if a[i] > a[i+1]:
        diff = a[i] - a[i+1]
        a[i+1] += diff
        ans += diff

print(ans)
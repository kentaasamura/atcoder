n, x, t = map(int, input().split())

a = n // x
b = n % x
d = a + 1 if b != 0 else a

ans = d * t

print(ans)
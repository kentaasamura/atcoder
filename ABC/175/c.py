x, k, d = map(int, input().split())

if abs(x) >= k * d:
    print(abs(x) - k * d)
else:
    q, mod = divmod(x, d)
    if (k - q) % 2 == 0:
        print(mod)
    else:
        print(abs(mod - d))

# Code for B - Almost GCD
# Use input() to fetch data from STDIN

n = int(input())
a = list(map(int, input().split()))  # n個の数字がリストに格納される

max_a = 2
for i in range(n):
    if max_a < a[i]:
        max_a = a[i]

max_count = 0
max_gcd = 2
for i in range(2, max_a + 1):
    count = 0
    for j in range(n):
        if a[j] % i == 0:
            count += 1
    if count >= max_count:
        max_count = count
        max_gcd = i

print(max_gcd)

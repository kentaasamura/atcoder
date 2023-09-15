# Code for D - Wandering
# Use input() to fetch data from STDIN

n = int(input())
a = list(map(int, input().split()))  # n個の数字がリストに格納される

x = 0
max_x = 0
for i in range(n):
    for j in range(i+1):
        x += a[j]
        if max_x < x:
            max_x = x

print(max_x)

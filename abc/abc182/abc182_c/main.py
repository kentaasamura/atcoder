# Code for C - To 3
# Use input() to fetch data from STDIN
n = int(input())

s = str(n)
array = list(map(int, s))
n_sum = sum(array)
if n_sum % 3 == 0:
    print(0)

# q, mod = divmod(n_sum, 3)
# print(q, mod)

# for i in range(n):
#     sum +=
#     if max_a < a[i]:
#         max_a = a[i]

# max_count = 0
# max_gcd = 2
# for i in range(2, max_a + 1):
#     count = 0
#     for j in range(n):
#         if a[j] % i == 0:
#             count += 1
#     if count >= max_count:
#         max_count = count
#         max_gcd = i

# print(max_gcd)


# print("Hello world")

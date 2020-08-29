s = input()
t = input()

l = len(s)-len(t)+1
c = [0] * l

for i in range(l):
    for j in range(len(t)):
        if s[i+j] != t[j]:
            c[i] += 1

print(min(c))

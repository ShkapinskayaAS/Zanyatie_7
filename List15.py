n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

b = []
s = 0

for i in range(1, len(a), 2):
    b.append(a[i])
    s = s + a[i]

print(b)
print(s)
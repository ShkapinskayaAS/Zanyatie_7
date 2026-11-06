n = int(input())
a = []

for i in range(n):
    a.append(int(input()))

s = 0

for x in a:
    s = s + x

average = s / len(a)

b = []

for x in a:
    if x > average:
        b.append(x)

print(b)
print(len(b))
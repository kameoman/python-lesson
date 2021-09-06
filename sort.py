# 昇順
n = int(input())
a = [0]*n

for i in range(n):
    a[i] = int(input())

a.sort()

for i in range(n):
    print(a[i])

#降順

n = int(input())

a = [0]*n

for i in range(n):
    a[i] = int(input())

a.sort(reverse=True)

for i in range(n):
    print(a[i])

#辞書型のソート

n = int(input())
ab = [None]*n

for i in range(n):
    [a,b] = input().split()
    a = int(a)
    b = int(b)
    ab[i] = [a,b]

ab.sort(reverse=True)

for i in range(n):
    [a,b] = ab[i]
    print(a,b)
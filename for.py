# 3の倍数のカウント
n = int(input())
a = input().split()

ans = 0

for i in range(n):
    if int(a[i]) % 3 == 0:
        ans += 1

print(i)
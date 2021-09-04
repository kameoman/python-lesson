# 3の倍数のカウント
# n = int(input())
# a = input().split()

# ans = 0

# for i in range(n):
#     if int(a[i]) % 3 == 0:
#         ans += 1

# print(i)

#フラグ管理

n = int(input())

flag = False

for i in range(n):
    a = int(input())
    if a == 7:
        flag = True

if flag:
    print("YES")
else:
    print("NO")
# # カンマ区切りの3つのデータの入力
# n = int(input())
# s = input().split(',')

# for i in range(n):
#     print(s[i])



# N個のデータの入力(横⇒縦)
# n = int(input())
# s = input().split()

# for i in range(n):
#     print(s[i])

# 3つのデータの入力(横⇒縦)
# s = input().split()
# print(s[0])
# print(s[1])
# print(s[2])


# n = int(input())

# A = [0]*n

# for i in range(n):
#     a = int(input())
#     A[i] = a

# print(A)
# print(max(A))

# 半角スペース区切りでの出力
# n = int(input())

# p = ["paiza"]*n

# print(" ".join(p))

# a = input()
# b = input()

# print("No" if b == "abc" else "yes")

# if b == "abc":
#   print("No")
# elif b == "xy":
#   print("No")
# else:
#   print("Yes")

# n = int(input())

# a = input().split()

# print(a)
# for i in range(n):
#     print(a[i])

# n = int(input())

# for i in range (n):
#   name = input().split()
#   print(name[0])
#   print(int(name[1])+1)

# nums = [2,7,11,15]
# target = 9
# result = []
# for i in range(len(nums)):
#   for j in range(i,len(nums)):
#     if nums[i] + nums[j] == target:
#       result = [i, j]
#       break;

# print(result)
x = 123

s = (x > 0) - (x < 0) #1(true)-0(false)
r = int(str(x*s)[::-1])
y = s*r * (r < 2**31) #321*1(true)

print (s)#1
print (r)#321
print (y)#321

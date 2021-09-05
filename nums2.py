# ②1から1234567890の約数の和 python
# numを1から36までの自然数で割り算し、余りが0の場合に出力していきます。
num = 1234567890
a = []
for i in range(1, num+1):
    if num % i == 0:
      a.append(i)

b = sum(a[0:5000000])

# 1734174
print(b)
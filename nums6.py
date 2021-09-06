# ⑥掛け算耐性
# 整数に対して、「一桁ことにばらして各桁の数字の積を求める」という操作を考えます。

# 123 → 1 × 2 × 3 = 6
# 666 → 6 × 6 × 6 = 216
# 1024 → 1 × 0 × 2 × 4 = 0
# 任意の整数について、「操作」を繰り返し適用すると、最終的には一桁の数に到達します。

# 77 → 49 → 36 → 18 → 8
# 123456 → 720 → 0
# 一桁の数に到達するのに必要な「操作」の回数は、77では4回、123456では2回となります。

# それでは、1000000以下の整数のうち、一桁の数に到達するのに必要な「操作」の回数が3回となるものはいくつあるかを、求めてください。



import functools
import operator


def product(num):
  count = 0
  while True:
    keta = [int(i) for i in list(str(num))]
    if len(keta) == 1:
     return count
    num = functools.reduce(operator.mul, keta)
    count += 1

print(len([i for i in range(1000001) if product(i) == 7]))

  # 2450
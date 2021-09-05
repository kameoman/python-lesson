# ④ピタゴラスな三角形
# 三辺の長さが3，4，5である三角形は直角三角形です。これは「ピタゴラスの定理」から示されます。

# 【ピタゴラスの定理】 直角三角形について、直角をはさむ2辺の長さがaとbで斜辺の長さがcであるとき a2 + b2 = c2 が成り立つ。
# つまり、32 + 42 = 52（ = 25）が成立するので直角三角形といえるのです。

# 三辺の長さが整数で面積が5000以下である直角三角形は何種類あるかを求めてください。

# ※合同なもの（例えば“3，4，5”と“5，4，3”）は区別せず1種類として数えます。

import math, itertools

def foo(n):
  max = 2 * n
  return sum([[[a, b, int(math.sqrt(a**2 + b**2))] \
    for b in range(1, math.ceil(max / a)) \
      if math.sqrt(a**2 + b**2).is_integer()] \
        for a in range(1, max + 1)], [])

def bar(list):
  listb = []
  while list != []:
    elm = list[0]
    list = [i for i in list if not tuple(i) in itertools.permutations(elm)]
    listb += [elm]
  return listb

print(len(bar(foo(5000))))

  # 105
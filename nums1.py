# ①1から64までの数をそれぞれ4乗した数の和

a=[]

for i in range (0,64):
  i += 1
  n = i**4
  a.append(n)

b = sum(a)

print(b)

# 問題1
# 4乗的ガウス
# 1から64までの整数の4乗の和を求めてください。

# 14 + 24 + 34 + ⋯ + 644
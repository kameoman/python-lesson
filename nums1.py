# ①1から64までの数をそれぞれ4乗した数の和

a=[]

for i in range (1,65):
  i += 1
  n = i**4
  a.append(n)

b = sum(a)

print(b)
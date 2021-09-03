# 4乗の和(1~64)

def suma():
  result = []
  for i in range(0,64):
        i += 1
        # print(i)
        n = i**4
        result.append(n)
  return result

ints = sum(suma())

# ants = (ints ** 2)



print (ints)

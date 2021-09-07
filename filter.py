# filter

def is_even(n):
  return n % 2 == 0

a = [10, 20, 30, 35]

print(list(filter(is_even,range(10))))

print(list(filter(is_even,a)))

#lambda式
print(list(filter(lambda n: n%2 == 0,a)))

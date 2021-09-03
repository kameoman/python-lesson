scores = [10,20,30]

num = scores[0:1]

print(int(num[0]))

for i in range(len(scores)):
  scores.append((i+200)**2)

print(scores)

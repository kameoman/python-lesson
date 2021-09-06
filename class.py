class User:
  def __init__(self,name,age=20):
      self.name = name
      self.age = age
  def age(self):
      print("{1}".format(self.age))

# no1 = User("bob")
no1 = User("bob")

print(no1.name,no1.age)

# no1.age()
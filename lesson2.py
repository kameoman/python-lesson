
import module.po1 as mp1

no1 = mp1.AdminUser("bob",20)

print(no1.name)
no1.say_hello()
no1.say_hi()

# 返り値
num = no1.game()
score = num ** 2

print(score)
# ICカードを使用し指定された回数バスに乗った時の残額を表示するプログラムを作成しています。
# 条件は以下の通りです。
# 1.運賃支払い時、運賃の10%がポイントとして入る。
# 2.バス乗車時、支払う運賃以上のポイントがある時、ポイントが優先して使われる。

print("所持金,乗車回数を入力してください:")
money,n = map(int,input().split())

point = 0

for i in range(n):
  print("乗車運賃を入力してください:")
  price = int(input())

  if point >= price:
    point -= price
  else:
    money = money - price
    point += int(price/10)
  
  print("残金", money,"ポイント数", point)
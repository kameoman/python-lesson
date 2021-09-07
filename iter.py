# イテレータとは、
# 連続するデータを操作するオブジェクト（リスト・集合・タプル）

# scores = [10, 20, 30, 40]
# it = iter(scores)
# print(next(it))
# print(next(it))
# print(next(it))
# print("hello")
# print(next(it))

# 上と同じ意味
# for score in scores:
#   print(score)

# ジェネレータ
# リストから変換するのではなくて 0 からイテレータを作ることもできます。0から連続するデータを操作するオブジェクト作ることをジェネレータ
# 無限ループを while True:
# 次の要素を引っ張ってくる yield i * 2 という命令 ジェネレータの重要なポイント
#yieldをnextと連動させて取ってくることができる。
# イテレータを作るこうした関数をジェネレータと呼ぶ

# def get_infinite():
#   i = 0
#   while True:
#     yield i * 2
#     i += 1

# g = get_infinite()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# for x in g:
#   print(x)


def point():
  i = 0
  while i < 10:
    yield i +2
    i += 2

no1 = point()
print(next(no1))
print(next(no1))
print(next(no1))
print(next(no1))

for g in no1:
  print(g)
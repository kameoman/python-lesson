# mapとlambda

def triple(n):
  return n * 3

print(list(map(triple,[1, 2, 3])))

a = [10, 20, 30]

# mapでリスト（イテレータ）を呼ぶとジェネレータになる。そのため結果をリストに変換する必要がある。
print(list(map(triple,a)))

#lambdaは上記の計算（triple）関数を書かなくても一行で実行できるものをいう。

print(list(map(lambda n: n*3, a)))

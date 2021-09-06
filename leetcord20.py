# 20. Valid Parentheses

# 文字 '（'、 '）'、 '{'、 '}'、 '['および ']'のみを含む文字列sが与えられた場合、入力文字列が有効かどうかを判別します。

# 入力文字列は、次の場合に有効です。

# 開いたブラケットは、同じタイプのブラケットで閉じる必要があります。
# 開いたブラケットは正しい順序で閉じる必要があります。

# Example 1:


#   Input: s = "()"
#   Output: true

# 考え方
# stack配列と辞書(map)を用意する。
# mapには対応する記号を入力
# 文字列を一文字ずつ見ていき、括弧の始まりならstackに追加し、閉じ括弧ならstackの直近のものを取り出して合っているかどうか確認。

# stackとdict(map)を定義する。
# dict = {"]":"[", "}":"{", ")":"("}
# for文で文字を一文字ずつみていきます。
class Solution:
  def isValid(self, s="()"):
      stack = []
      dict = {"]":"[", "}":"{", ")":"("}
      for char in s:
          if char in dict.values(): #括弧始まりかどうかTrue
              stack.append(char)
          elif char in dict.keys(): #括弧終わりかどうかTrueの時さらに条件
              if stack == [] or dict[char] != stack.pop(): #
                  return False
          else:
              return False
      return stack == []

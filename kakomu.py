# 標準入力で出力する文字列を枠で囲む装飾をするプログラムを書きたいです。

# 例
# +++++++
# +arist+
# +++++++
# ↑のようになるプログラムを書きたいです。

input_text = input()

str_len = len(input_text)

print("="*(str_len +2))
print("<"+input_text+">")
print("="*(str_len +2))

# =======
# <qiita>
# =======
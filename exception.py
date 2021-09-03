
class MyException(Exception):
  pass

def div(a,b):
  try:
    if (b <0):
      raise MyException("マイナスでは計算が出来ません")
    print(a/b)
  except ZeroDivisionError:
    print("計算できません")
  except MyException as e:
    print(e)
  else:
    print("計算完了しました")


div(10,-2)
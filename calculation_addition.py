# Python sample Calculate Addition

# sysモジュール インポート
import sys

# 初期化
result = 0

# 引数
args = sys.argv

# 引数チェック 個数
if len(args) != 3:
  print('引数は2個入力してください')
  sys.exit()

# 引数チェック 数値
if args[1].isdigit() and args[2].isdigit():
  # 計算
  result = int(args[1]) + int(args[2])
else:
  print('引数が数値ではありません')
  sys.exit()

# 出力
print('This is ' + args[0])
print('引数1：' + args[1])
print('引数2：' + args[2])
print('合計：' + str(result))

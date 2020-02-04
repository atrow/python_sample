# Python sample Calculate Addition

# sysモジュール インポート
import sys

# 引数
args = sys.argv

# 計算
result = int(args[1]) + int(args[2])

# 出力
print('This is ' + args[0])
print('引数1：' + args[1])
print('引数2：' + args[2])
print('合計：' + str(result))

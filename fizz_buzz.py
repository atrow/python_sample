# Python sample Fizz Buzz

# 入力メッセージ
print('Fizz Buzz を開始します')
print('上限値を入力してください')

# 入力値受付
while True:

  # 入力値
  var = input()

  if var.isdigit():
    # ループ終了
    print('')
    break
  else:
    # 再度入力
    print('数値を入力してください')

# ループ
for i in range(int(var) + 1):
  # 出力用変数初期化
  result = ''

  # Fizz Buzz 判定
  if i % 3 == 0:
    result = result + 'Fizz'
  if i % 5 == 0:
    result = result + 'Buzz'

  if len(result) == 0:
    # FizzでもBuzzでもない場合、数値出力
    print(i)
    # ループ継続
    continue

  # 出力
  print(result)

else:
  # 終了メッセージ
  print('Fizz Buzz が終了しました')

result = (1, 2, 3, 4, 5) + (1, 2, 3, 4, 5)
print(result)

# 8の倍数を出力する場合
tp1 = (4, 8, 12, 16, 20, 24, 28, 32, 36, 40)
tp2 = (4, 8, 12, 16, 20, 24, 28, 32, 36, 40)
result = [x + y for (x, y) in zip(tp1, tp2)]
print(result)

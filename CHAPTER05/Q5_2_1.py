num = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
col = [row[2] for row in num]
print(col)

# 2, 3, 7, 8を出力
num = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]
col = [row[2:4] for row in num]
print(col)

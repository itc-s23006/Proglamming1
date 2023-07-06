def print_diagonal_square(n):
    # 4×4の正方形の要素数が16個であることを確認
    assert n == 16, "正方形の要素数は16個である必要があります。"

    # 4×4の正方形状に要素を配置し、対角線上を●に変更する
    square = [["◯" for _ in range(4)] for _ in range(4)]
    for i in range(4):
        square[i][i] = "●"

    # 文字列として正方形を表示
    for row in square:
        print(" ".join(row))


# 4×4の正方形を表示
print_diagonal_square(16)

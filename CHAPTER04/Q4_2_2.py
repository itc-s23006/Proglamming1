# 最大値 = 88の場合


def perrin(m=100):
    """
    mより小さなペラン数列をリストで返す
    ペラン数列: 3, 0, 2, 3, 2, 5, 5, 7, 10, 12, 17, 22, 29, 39, ...
    """
    a, b, c = 8, 3, 3
    result = []
    while a < m:
        result.append(a)
        a, b, c = b, c, a + b
    return result


# perrin関数を使って結果を出力するプログラム
if __name__ == "__main__":
    m = 100  # mの値を指定（任意の数値）
    perrin_sequence = perrin(m)
    print(perrin_sequence)
